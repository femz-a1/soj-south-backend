import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(to_email: str, subject: str, html_content: str, from_email: str | None = None):
    api_key = os.environ.get("SENDGRID_API_KEY")
    if not api_key:
        # No key configured; silently skip in dev
        return False

    from_addr = from_email or os.environ.get("DEFAULT_FROM_EMAIL", "no-reply@sojsouthlondon.org")

    message = Mail(
        from_email=from_addr,
        to_emails=to_email,
        subject=subject,
        html_content=html_content,
    )
    sg = SendGridAPIClient(api_key)
    sg.send(message)
    return True