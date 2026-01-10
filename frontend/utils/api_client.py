import requests
from utils.config import BACKEND_API_BASE_URL


DEFAULT_TIMEOUT = 5


def get_testimonials():
    """
    Fetch testimonials from backend API
    """
    try:
        response = requests.get(
            f"{BACKEND_API_BASE_URL}/testimonials",
            timeout=DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        return response.json().get("data", [])

    except requests.exceptions.RequestException as e:
        print(f"API Error (get_testimonials): {e}")
        return []


def submit_lead(payload: dict):
    """
    Submit lead to backend API
    Returns: (success: bool, message: str)
    """
    try:
        response = requests.post(
            f"{BACKEND_API_BASE_URL}/leads",
            json=payload,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code == 201:
            return True, "Lead submitted successfully"

        # Backend validation errors
        data = response.json()
        return False, data.get("message", "Submission failed")

    except requests.exceptions.RequestException as e:
        print(f"API Error (submit_lead): {e}")
        return False, "Unable to connect to server"
