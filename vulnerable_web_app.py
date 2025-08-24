"""
Vulnerable Flask Web Application - Educational Purpose Only
Contains multiple security vulnerabilities for testing security scanners
"""

from flask import Flask, request, render_template_string, jsonify, redirect
import os
import subprocess
import pickle
import yaml
import sqlite3
import hashlib

app = Flask(__name__)

# VULNERABILITY: Hardcoded secret key
app.secret_key = "super_secret_key_123"

# VULNERABILITY: Debug mode in production
app.config['DEBUG'] = True

# VULNERABILITY: Hardcoded database credentials
DATABASE_URL = "postgresql://admin:password123@localhost/myapp"
API_KEY = "sk-1234567890abcdef"  # Hardcoded API key

@app.route('/')
def index():
    return """
    <h1>Vulnerable Web App</h1>
    <p>This app contains intentional vulnerabilities for security testing.</p>
    <ul>
        <li><a href="/search?q=test">Search (SQL Injection)</a></li>
        <li><a href="/render?template=<h1>Hello</h1>">Template (XSS)</a></li>
        <li><a href="/files?path=../etc/passwd">Files (Path Traversal)</a></li>
        <li><a href="/exec?cmd=ls">Execute (Command Injection)</a></li>
    </ul>
    """

@app.route('/search')
def search():
    """VULNERABILITY: SQL Injection"""
    query = request.args.get('q', '')
    
    # Direct string concatenation - SQL injection vulnerability
    sql = f"SELECT * FROM users WHERE name LIKE '%{query}%'"
    
    # Simulate database query
    return f"Searching for: {query}<br>SQL: {sql}"

@app.route('/render')
def render_template():
    """VULNERABILITY: Server-Side Template Injection (SSTI)"""
    template = request.args.get('template', 'Hello World')
    
    # Direct template rendering without escaping - SSTI vulnerability
    return render_template_string(template)

@app.route('/files')
def get_file():
    """VULNERABILITY: Path Traversal"""
    file_path = request.args.get('path', 'default.txt')
    
    # No path validation - path traversal vulnerability
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return f"Error reading file: {e}"

@app.route('/exec')
def execute_command():
    """VULNERABILITY: Command Injection"""
    cmd = request.args.get('cmd', 'echo hello')
    
    # Direct command execution - command injection vulnerability
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return f"<pre>{result}</pre>"
    except Exception as e:
        return f"Error: {e}"

@app.route('/eval')
def evaluate_code():
    """VULNERABILITY: Code Injection"""
    code = request.args.get('code', '2+2')
    
    # Using eval on user input - code injection vulnerability
    try:
        result = eval(code)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

@app.route('/deserialize', methods=['POST'])
def deserialize_data():
    """VULNERABILITY: Unsafe Deserialization"""
    data = request.get_data()
    
    try:
        # Unsafe pickle deserialization - RCE vulnerability
        obj = pickle.loads(data)
        return f"Deserialized: {obj}"
    except Exception as e:
        return f"Error: {e}"

@app.route('/yaml_load', methods=['POST'])
def load_yaml():
    """VULNERABILITY: Unsafe YAML Loading"""
    yaml_data = request.get_data(as_text=True)
    
    try:
        # Unsafe YAML loading - code execution vulnerability
        config = yaml.load(yaml_data)
        return jsonify(config)
    except Exception as e:
        return f"Error: {e}"

@app.route('/login', methods=['POST'])
def login():
    """VULNERABILITY: Weak Password Hashing"""
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    # Weak MD5 hashing - should use bcrypt or similar
    password_hash = hashlib.md5(password.encode()).hexdigest()
    
    # More SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password_hash}'"
    
    return f"Login attempt for: {username}"

@app.route('/redirect')
def unsafe_redirect():
    """VULNERABILITY: Open Redirect"""
    url = request.args.get('url', '/')
    
    # No URL validation - open redirect vulnerability
    return redirect(url)

@app.route('/xss')
def xss_demo():
    """VULNERABILITY: Cross-Site Scripting"""
    user_input = request.args.get('input', 'default')
    
    # Direct output without escaping - XSS vulnerability
    return f"<h1>Welcome {user_input}!</h1>"

# VULNERABILITY: Debug route that exposes sensitive information
@app.route('/debug')
def debug_info():
    """Exposes sensitive system information"""
    return {
        'environment_variables': dict(os.environ),
        'secret_key': app.secret_key,
        'database_url': DATABASE_URL,
        'api_key': API_KEY,
        'python_path': os.sys.path
    }

if __name__ == '__main__':
    # VULNERABILITY: Running with debug=True and host='0.0.0.0'
    app.run(debug=True, host='0.0.0.0', port=5000)
