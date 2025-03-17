import pytest
import os
from unittest.mock import patch
from src.smtp_email_sender import send_email
import smtplib

class MockSMTP:
    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def starttls(self):
        pass

    def login(self, username, password):
        pass

    def sendmail(self, *args):
        pass

def mock_env_vars(monkeypatch):
    monkeypatch.setenv('SMTP_SERVER', 'smtp.test.com')
    monkeypatch.setenv('SMTP_PORT', '587')
    monkeypatch.setenv('SMTP_USERNAME', 'testuser')
    monkeypatch.setenv('SMTP_PASSWORD', 'testpass')
    monkeypatch.setenv('EMAIL_FROM', 'sender@test.com')

def test_send_email_success(monkeypatch):
    mock_env_vars(monkeypatch)
    
    with patch('smtplib.SMTP', MockSMTP):
        result = send_email('recipient@test.com', 'Test Subject', 'Test Body')
        assert result is True

def test_send_email_missing_required_params():
    with pytest.raises(ValueError, match="to_email, subject, and body are required"):
        send_email('', '', '')

def test_send_email_missing_config(monkeypatch):
    monkeypatch.delenv('SMTP_SERVER', raising=False)
    
    with pytest.raises(ValueError, match="Missing SMTP configuration"):
        send_email('recipient@test.com', 'Test Subject', 'Test Body')

@patch('smtplib.SMTP')
def test_send_email_smtp_exception(mock_smtp, monkeypatch):
    mock_env_vars(monkeypatch)
    
    mock_smtp.side_effect = smtplib.SMTPException("SMTP Error")
    
    with pytest.raises(smtplib.SMTPException):
        send_email('recipient@test.com', 'Test Subject', 'Test Body')