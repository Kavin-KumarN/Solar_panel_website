import re
from backend.models.lead_model import create_lead
from backend.services.email_service import send_admin_notification


def is_valid_phone(phone: str) -> bool:
    """Validate phone number (10–15 digits)"""
    return bool(re.fullmatch(r"\d{10,15}", phone))


def is_valid_email(email: str) -> bool:
    """Validate email format"""
    if not email:
        return True
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))


def validate_lead_data(data: dict):
    """Validate incoming lead data"""
    required_fields = ["name", "phone", "user_type"]

    for field in required_fields:
        if not data.get(field):
            return False, f"{field} is required"

    if not is_valid_phone(data["phone"]):
        return False, "Invalid phone number"

    if not is_valid_email(data.get("email")):
        return False, "Invalid email address"

    if data["user_type"] not in ["Residential", "Commercial", "Industrial"]:
        return False, "Invalid user type"

    return True, None


def process_lead(data: dict):
    """Main business function to process a lead"""

    is_valid, error = validate_lead_data(data)
    if not is_valid:
        return False, error

    lead_record = {
        "name": data.get("name"),
        "phone": data.get("phone"),
        "email": data.get("email"),
        "location": data.get("location"),
        "user_type": data.get("user_type"),
        "message": data.get("message"),
    }

    success = create_lead(**lead_record)

    if not success:
        return False, "Failed to save lead"

    # Email notification should never block lead saving
    try:
        send_admin_notification(lead_record)
    except Exception as e:
        print(f"Email notification failed: {e}")

    return True, "Lead submitted successfully"


if __name__ == "__main__":
    test_data = {
        "name": "Service Test",
        "phone": "9876543210",
        "email": "service@test.com",
        "location": "Coimbatore",
        "user_type": "Commercial",
        "message": "Testing service layer"
    }

    success, msg = process_lead(test_data)
    print(success, msg)
