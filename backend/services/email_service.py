import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from backend.config import Config


def send_admin_notification(lead: dict):
    """
    Send email to admin when a new lead is received
    """
    msg = MIMEMultipart()
    msg["From"] = Config.EMAIL_USER
    msg["To"] = Config.ADMIN_EMAIL
    msg["Subject"] = "New Solar Lead Received"

    body = f"""
New Solar Enquiry Received:

Name: {lead['name']}
Phone: {lead['phone']}
Email: {lead.get('email', 'N/A')}
Location: {lead.get('location', 'N/A')}
Customer Type: {lead['user_type']}
Message: {lead.get('message', '')}
"""

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT)
        server.starttls()
        server.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

if __name__ == "__main__":
    test_lead = {
        "name": "Test User",
        "phone": "9999999999",
        "email": "test@example.com",
        "location": "Test City",
        "user_type": "Residential",
        "message": "Testing email service"
    }

    result = send_admin_notification(test_lead)
    print("Email sent:", result)
