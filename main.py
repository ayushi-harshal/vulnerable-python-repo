#!/usr/bin/env python3
"""
Simple Flask Application for CodeArmor Testing
Contains 3 key vulnerabilities that are easy for AI to fix
"""

from flask import Flask, jsonify, request
import yaml
from database import UserDatabase

# Create Flask app
app = Flask(__name__)

# VULNERABILITY 1: Hardcoded secret key (should use environment variable)
app.config['SECRET_KEY'] = 'hardcoded-insecure-key-12345'

# Initialize database
db = UserDatabase()

@app.route('/search')
def search_user():
    """Endpoint that uses vulnerable SQL injection method"""
    username = request.args.get('username', '')
    # This calls the vulnerable method in database.py
    users = db.search_user(username)
    return jsonify({"users": users})

@app.route('/config', methods=['POST'])
def load_config():
    """VULNERABILITY 3: Unsafe YAML loading - can execute arbitrary code"""
    config_data = request.get_data(as_text=True)
    # Unsafe YAML loading - should use yaml.safe_load()
    config = yaml.load(config_data, Loader=yaml.FullLoader)
    return jsonify({"config": config})

@app.route('/')
def index():
    """Basic home endpoint"""
    return jsonify({
        "message": "Vulnerable Flask App for CodeArmor Testing",
        "vulnerabilities": [
            "1. Hardcoded secret key",
            "2. SQL injection in /search endpoint", 
            "3. Unsafe YAML loading in /config endpoint"
        ],
        "endpoints": [
            "/search?username=admin",
            "/config (POST with YAML data)"
        ]
    })

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',  # Only bind to localhost
        port=5000,
        debug=False        # Debug mode disabled
    )
