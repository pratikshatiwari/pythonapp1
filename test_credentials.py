# test_credentials.py
ADMIN_PASSWORD = "admin123"  # Should be detected
USER_TOKEN = "secret_token"  # Should be detected
API_KEY = "abc123"  # Should be detected in scan

def login():
    username = "admin1"  # Should be detected
    password = "password123"  # Should be detected
    return username, password
