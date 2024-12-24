from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
import os
import f

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # FLAG: Potential security issue

# SECURITY ISSUE: Hardcoded credentials
CREDENTIALS = {
    "admin": {
        "username": "admin",  # SECURITY ISSUE: Hardcoded username
        "password": "admin1234",  # SECURITY ISSUE: Hardcoded password
        "role": "admin"
    },
    "user": {
        "username": "user",  # SECURITY ISSUE: Hardcoded username
        "password": "user123",  # SECURITY ISSUE: Hardcoded password
        "role": "user"
    }
}

# Website details
website_info = {
    "name": "My Awesome Website",
    "description": "Welcome to our amazing website!",
    "contact_email": "contact@example.com",
    "address": "123 Main Street, City, Country",
    "phone": "+1 234 567 890"
}

# app.py
hardcoded_password = "mySuperSecretPassword"
secret_token = "myToken12345"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # SECURITY ISSUE: Direct credential comparison
        user_data = CREDENTIALS.get(username)
        if user_data and user_data["password"] == password:
            session['username'] = username
            session['role'] = user_data["role"]
            flash(f'Welcome {user_data["role"].title()}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')

    # app.py

def count_lines(file_path):
    """
    Counts the number of lines in a given file.

    Args:
        file_path (str): Path to the file.

    Returns:
        int: Number of lines in the file.
    """
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

def contains_keyword(file_path, keyword):
    """
    Checks if a given keyword exists in the file.

    Args:
        file_path (str): Path to the file.
        keyword (str): Keyword to search for.

    Returns:
        bool: True if keyword is found, False otherwise.
    """
    with open(file_path, 'r') as file:
        return any(keyword in line for line in file)

    
    return render_template('login.html')
