from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # In production, use environment variable

# Hardcoded users (In production, use a database)
users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin",
        "email": "admin@example.com"
    },
    "user1": {
        "password": generate_password_hash("user123"),
        "role": "user",
        "email": "user1@example.com"
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

# Login decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Admin decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session or users[session['username']]['role'] != 'admin':
            flash('Admin access required', 'error')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html', website_info=website_info)

@app.route('/about')
def about():
    return render_template('about.html', website_info=website_info)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you would typically process the contact form
        flash('Thank you for your message!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', website_info=website_info)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            session['role'] = users[username]['role']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if username in users:
            flash('Username already exists', 'error')
        else:
            users[username] = {
                "password": generate_password_hash(password),
                "role": "user",
                "email": email
            }
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_data = users[session['username']]
    return render_template('dashboard.html', user_data=user_data)

@app.route('/admin')
@login_required
@admin_required
def admin_panel():
    return render_template('admin.html', users=users)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        email = request.form.get('email')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        
        user = users[session['username']]
        
        if check_password_hash(user['password'], current_password):
            if new_password:
                user['password'] = generate_password_hash(new_password)
            user['email'] = email
            flash('Profile updated successfully', 'success')
        else:
            flash('Current password is incorrect', 'error')
            
    return render_template('profile.html', user=users[session['username']])

# API endpoints
@app.route('/api/users', methods=['GET'])
@login_required
@admin_required
def api_users():
    safe_users = {
        username: {
            "role": data["role"],
            "email": data["email"]
        } for username, data in users.items()
    }
    return jsonify(safe_users)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
