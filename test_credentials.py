# test_credentials.py
ADMIN_PASSWORD = "admin123"  # Should be detected
USER_TOKEN = "secret_token"  # Should be detected
API_KEY = "abc123"  # Should be detected

def login():
    username = "admin"  # Should be detected
    password = "password123"  # Should be detected
    return username, password
