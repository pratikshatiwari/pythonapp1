# test_credentials.py
ADMIN_PASSWORD = "admin123"  # Should be detected
USER_TOKEN = "secret_token"  # Should be detected
API_KEY = "abc123"  # Should be detected in scan

# test_credentials.py
PASSWORD = "my_secret_password"
API_KEY = "abcd1234token"
SECRET_KEY = "super_secret_key"

def login():
    username = "admin1"  # Should be detected
    password = "password123"  # Should be detected
    return username, password
