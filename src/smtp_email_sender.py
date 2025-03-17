import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

def send_email(to_email, subject, body, from_email=None):
    """
    Send an email using SMTP protocol.

    Args:
        to_email (str): Recipient's email address
        subject (str): Email subject
        body (str): Email body content
        from_email (str, optional): Sender's email address. 
                                    Defaults to environment variable EMAIL_FROM.

    Raises:
        ValueError: If required email configuration is missing
        SMTPException: For any SMTP-related errors during email sending

    Returns:
        bool: True if email sent successfully
    """
    # Validate inputs
    if not to_email or not subject or not body:
        raise ValueError("to_email, subject, and body are required")

    # Use environment variables for configuration
    from_email = from_email or os.getenv('EMAIL_FROM')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Check for missing configuration
    if not all([from_email, smtp_server, smtp_username, smtp_password]):
        raise ValueError("Missing SMTP configuration. Check environment variables.")

    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Establish secure connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, message.as_string())

        return True

    except smtplib.SMTPException as e:
        raise SMTPException(f"Failed to send email: {str(e)}")