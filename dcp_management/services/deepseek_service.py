import frappe
import requests
import base64
import time
import json
import mimetypes
import os

def get_api_key():
    """Fetches the DeepSeek API key from DCP Settings."""
    api_key = frappe.db.get_single_value('DCP Settings', 'deepseek_api_key', cache=True)
    if not api_key:
        frappe.throw("DeepSeek API Key is not set in DCP Settings.")
    return api_key

def get_vision_model():
    """Fetches the configured DeepSeek vision model from DCP Settings."""
    model = frappe.db.get_single_value('DCP Settings', 'deepseek_model', cache=True)
    return model or "deepseek-vl-chat"

def _save_ai_log(status, model, duration, file_url, prompt, http_status_code=None,
                 response=None, raw_response=None, error_details=None,
                 reference_doctype=None, reference_name=None):
    """Persist one DCP AI Log record. Runs in the same transaction as the caller."""
    try:
        log = frappe.get_doc({
            "doctype": "DCP AI Log",
            "status": status,
            "model": model,
            "duration_seconds": round(duration, 2),
            "file_url": file_url,
            "prompt": prompt,
            "http_status_code": http_status_code,
            "response": response,
            "raw_response": json.dumps(raw_response, indent=2) if raw_response else None,
            "error_details": error_details,
            "reference_doctype": reference_doctype,
            "reference_name": reference_name,
            "requested_by": frappe.session.user,
        })
        log.insert(ignore_permissions=True)
        frappe.db.commit()
    except Exception as log_err:
        # Never let logging break the main flow
        frappe.log_error(f"Failed to save DCP AI Log: {log_err}", "DCP AI Log Error")

def _read_file_as_base64(file_url):
    """
    Reads a file and returns (base64_string, mime_type).
    - For Frappe private files (/private/files/...) reads directly from disk — no auth needed.
    - For Frappe public files (/files/...) reads from the public directory on disk.
    - For external URLs falls back to an HTTP GET.
    """
    # Strip query string / fragment
    clean_url = file_url.split('?')[0].split('#')[0]
    mime, _ = mimetypes.guess_type(clean_url)
    mime = mime or 'image/jpeg'

    if clean_url.startswith('/private/files/'):
        filename = clean_url[len('/private/files/'):]
        file_path = frappe.get_site_path('private', 'files', filename)
    elif clean_url.startswith('/files/'):
        filename = clean_url[len('/files/'):]
        file_path = frappe.get_site_path('public', 'files', filename)
    else:
        file_path = None

    if file_path:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found on disk: {file_path}")
        with open(file_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8'), mime

    # External URL — fetch over HTTP
    response = requests.get(file_url, stream=True, timeout=30)
    response.raise_for_status()
    return base64.b64encode(response.content).decode('utf-8'), mime


def analyze_document_with_vision(file_url, prompt, reference_doctype=None, reference_name=None):
    """
    Analyzes an image using the DeepSeek Vision model.

    :param file_url: The public URL of the image file.
    :param prompt: The prompt to guide the analysis.
    :return: The analysis result from the AI.
    """
    api_key = get_api_key()
    model = get_vision_model()
    start = time.time()

    # Read the image from disk or via HTTP
    try:
        encoded_image, mime_type = _read_file_as_base64(file_url)
    except Exception as e:
        duration = time.time() - start
        err = f"Failed to read image: {e}"
        frappe.log_error(err, "DeepSeek Service Error")
        _save_ai_log(
            status="Image Download Failed", model=model, duration=duration,
            file_url=file_url, prompt=prompt, error_details=err,
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return "Error: Could not retrieve the document image for analysis."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{encoded_image}"}}
                ]
            }
        ],
        "max_tokens": 1024
    }

    try:
        api_response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
        duration = time.time() - start
        raw = None
        try:
            raw = api_response.json()
        except Exception:
            pass
        api_response.raise_for_status()
        extracted = raw['choices'][0]['message']['content']
        _save_ai_log(
            status="Success", model=model, duration=duration,
            file_url=file_url, prompt=prompt,
            http_status_code=api_response.status_code,
            response=extracted, raw_response=raw,
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return extracted
    except requests.exceptions.RequestException as e:
        duration = time.time() - start
        err_msg = str(e)
        raw = None
        http_code = None
        try:
            raw = api_response.json()
            http_code = api_response.status_code
            err_msg = raw.get('error', {}).get('message', err_msg)
        except Exception:
            pass
        frappe.log_error(f"DeepSeek API request failed: {e}", "DeepSeek Service Error")
        _save_ai_log(
            status="Error", model=model, duration=duration,
            file_url=file_url, prompt=prompt,
            http_status_code=http_code, raw_response=raw,
            error_details=f"{e}",
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return f"Error communicating with DeepSeek API: {err_msg}"
    except (KeyError, IndexError) as e:
        duration = time.time() - start
        frappe.log_error(f"Unexpected DeepSeek API response format: {raw}", "DeepSeek Service Error")
        _save_ai_log(
            status="Error", model=model, duration=duration,
            file_url=file_url, prompt=prompt,
            http_status_code=getattr(api_response, 'status_code', None),
            raw_response=raw, error_details=f"Unexpected response format: {e}",
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return "Error: The response from the AI was in an unexpected format."

def get_chat_completion(messages, model="deepseek-chat", reference_doctype=None, reference_name=None):
    """
    Gets a chat completion from the DeepSeek API.

    :param messages: A list of message objects (e.g., [{"role": "user", "content": "Hello"}]).
    :param model: The model to use (e.g., 'deepseek-chat' or 'deepseek-coder').
    :return: The chat completion response.
    """
    api_key = get_api_key()
    start = time.time()
    prompt_summary = " | ".join(m.get('content', '')[:200] for m in messages if isinstance(m.get('content'), str))

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 2048,
        "temperature": 0.7,
    }

    try:
        api_response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
        duration = time.time() - start
        raw = None
        try:
            raw = api_response.json()
        except Exception:
            pass
        api_response.raise_for_status()
        extracted = raw['choices'][0]['message']['content']
        _save_ai_log(
            status="Success", model=model, duration=duration,
            file_url=None, prompt=prompt_summary,
            http_status_code=api_response.status_code,
            response=extracted, raw_response=raw,
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return extracted
    except requests.exceptions.RequestException as e:
        duration = time.time() - start
        err_msg = str(e)
        raw = None
        http_code = None
        try:
            raw = api_response.json()
            http_code = api_response.status_code
            err_msg = raw.get('error', {}).get('message', err_msg)
        except Exception:
            pass
        frappe.log_error(f"DeepSeek API request failed: {e}", "DeepSeek Service Error")
        _save_ai_log(
            status="Error", model=model, duration=duration,
            file_url=None, prompt=prompt_summary,
            http_status_code=http_code, raw_response=raw,
            error_details=f"{e}",
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return f"Error communicating with DeepSeek API: {err_msg}"
    except (KeyError, IndexError) as e:
        duration = time.time() - start
        frappe.log_error(f"Unexpected DeepSeek API response format: {raw}", "DeepSeek Service Error")
        _save_ai_log(
            status="Error", model=model, duration=duration,
            file_url=None, prompt=prompt_summary,
            http_status_code=getattr(api_response, 'status_code', None),
            raw_response=raw, error_details=f"Unexpected response format: {e}",
            reference_doctype=reference_doctype, reference_name=reference_name,
        )
        return "Error: The response from the AI was in an unexpected format."
