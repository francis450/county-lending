import frappe
import requests
import base64

def get_api_key():
    """Fetches the DeepSeek API key from DCP Settings."""
    api_key = frappe.db.get_single_value('DCP Settings', 'deepseek_api_key', cache=True)
    if not api_key:
        frappe.throw("DeepSeek API Key is not set in DCP Settings.")
    return api_key

def analyze_document_with_vision(file_url, prompt):
    """
    Analyzes an image using the DeepSeek Vision model.

    :param file_url: The public URL of the image file.
    :param prompt: The prompt to guide the analysis.
    :return: The analysis result from the AI.
    """
    api_key = get_api_key()
    
    # Download the image and encode it to base64
    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()
        encoded_image = base64.b64encode(response.content).decode('utf-8')
    except requests.exceptions.RequestException as e:
        frappe.log_error(f"Failed to download image for analysis: {e}", "DeepSeek Service Error")
        return "Error: Could not retrieve the document image for analysis."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "deepseek-vl-chat",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 1024
    }

    try:
        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        frappe.log_error(f"DeepSeek API request failed: {e}", "DeepSeek Service Error")
        # Try to parse the error response from DeepSeek
        try:
            error_details = response.json()
            return f"Error communicating with DeepSeek API: {error_details.get('error', {}).get('message', 'Unknown error')}"
        except Exception:
            return f"Error communicating with DeepSeek API: {e}"
    except (KeyError, IndexError) as e:
        frappe.log_error(f"Unexpected DeepSeek API response format: {response.text}", "DeepSeek Service Error")
        return "Error: The response from the AI was in an unexpected format."

def get_chat_completion(messages, model="deepseek-chat"):
    """
    Gets a chat completion from the DeepSeek API.

    :param messages: A list of message objects (e.g., [{"role": "user", "content": "Hello"}]).
    :param model: The model to use (e.g., 'deepseek-chat' or 'deepseek-coder').
    :return: The chat completion response.
    """
    api_key = get_api_key()
    
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
        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        frappe.log_error(f"DeepSeek API request failed: {e}", "DeepSeek Service Error")
        try:
            error_details = response.json()
            return f"Error communicating with DeepSeek API: {error_details.get('error', {}).get('message', 'Unknown error')}"
        except Exception:
            return f"Error communicating with DeepSeek API: {e}"
    except (KeyError, IndexError) as e:
        frappe.log_error(f"Unexpected DeepSeek API response format: {response.text}", "DeepSeek Service Error")
        return "Error: The response from the AI was in an unexpected format."
