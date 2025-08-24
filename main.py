#!/usr/bin/env python3
"""
Vulnerable Flask Application for CodeArmor Testing
Contains intentional security vulnerabilities for AI fixing demonstration
"""

import os
import subprocess
import sqlite3
from flask import Flask, jsonify, request, render_template_string
import pickle
import yaml

# Create Flask app
app = Flask(__name__)

# VULNERABILITY 1: Hardcoded secret key
app.config['SECRET_KEY'] = 'hardcoded-insecure-key-12345'

# VULNERABILITY 2: SQL Injection vulnerability
def get_user_data(user_id):
    """Vulnerable to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # SQL Injection vulnerability - user input directly concatenated
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# VULNERABILITY 3: Command injection vulnerability
@app.route('/ping')
def ping_server():
    """Vulnerable to command injection"""
    host = request.args.get('host', 'localhost')
    # Command injection vulnerability - user input directly passed to shell
    result = subprocess.run(f"ping -c 4 {host}", shell=True, capture_output=True, text=True)
    return jsonify({"output": result.stdout, "error": result.stderr})

# VULNERABILITY 4: Pickle deserialization (unsafe)
@app.route('/load_data', methods=['POST'])
def load_data():
    """Vulnerable to pickle deserialization attacks"""
    data = request.get_data()
    # Unsafe pickle deserialization
    obj = pickle.loads(data)
    return jsonify({"loaded": str(obj)})

# VULNERABILITY 5: YAML unsafe loading
@app.route('/config', methods=['POST'])
def load_config():
    """Vulnerable to YAML code execution"""
    config_data = request.get_data(as_text=True)
    # Unsafe YAML loading - can execute arbitrary code
    config = yaml.load(config_data, Loader=yaml.Loader)
    return jsonify({"config": config})

# VULNERABILITY 6: Server-Side Template Injection (SSTI)
@app.route('/render')
def render_template():
    """Vulnerable to Server-Side Template Injection"""
    template = request.args.get('template', 'Hello World')
    # Direct template rendering without sanitization
    return render_template_string(template)

# VULNERABILITY 7: Path traversal
@app.route('/read_file')
def read_file():
    """Vulnerable to path traversal"""
    filename = request.args.get('filename')
    # No path validation - allows reading any file
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def index():
    """Basic home endpoint"""
    return jsonify({
        "message": "Vulnerable Flask App for CodeArmor Testing",
        "endpoints": [
            "/ping?host=example.com",
            "/load_data (POST)",
            "/config (POST)", 
            "/render?template=<template>",
            "/read_file?filename=<path>"
        ]
    })

if __name__ == '__main__':
    # Insecure configuration
    app.run(
        host='0.0.0.0',  # Binds to all interfaces - insecure
        port=5000,
        debug=True       # Debug mode enabled - insecure
    )
