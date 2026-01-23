import { FrappeApp } from 'frappe-js-sdk'

// Initialize Frappe SDK
const frappe = new FrappeApp(window.location.origin)

// Export Frappe SDK instance and methods
export const frappeClient = frappe
export const call = frappe.call()
export const db = frappe.db()
export const auth = frappe.auth()

// Get CSRF token from cookies
export const getCsrfToken = () => {
  const cookies = document.cookie.split(';')
  for (let cookie of cookies) {
    const [name, value] = cookie.trim().split('=')
    if (name === 'csrf_token') {
      return decodeURIComponent(value)
    }
  }
  return null
}

export const logout = async () => {
  const csrfToken = getCsrfToken()
  try {
    await fetch('/api/method/logout', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': csrfToken || ''
      }
    })
  } catch (e) {
    console.warn('Logout request failed', e)
  }
}

// Legacy API wrapper for backward compatibility
export const api = {
  async get(url) {
    const method = url.replace('/api/method/', '')
    return call.get(method)
  },

  async post(url, data) {
    const method = url.replace('/api/method/', '')
    
    // For guest endpoints, use fetch directly with CSRF token
    const csrfToken = getCsrfToken()
    
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': csrfToken || ''
      },
      credentials: 'include',
      body: JSON.stringify(data)
    }).then(r => r.json())
  },

  async upload(url, formData) {
    // For file uploads, include CSRF token
    const csrfToken = getCsrfToken()
    
    if (csrfToken) {
      formData.append('csrf_token', csrfToken)
    }
    
    return fetch(url, {
      method: 'POST',
      body: formData,
      credentials: 'include',
      headers: {
        'X-Frappe-CSRF-Token': csrfToken || ''
      }
    }).then(r => r.json())
  }
}
