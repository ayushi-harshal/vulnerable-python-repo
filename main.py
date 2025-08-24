#!/usr/bin/env python3
"""
Ultra-minimal Flask application for CodeQL testing
This is the simplest possible Flask app with zero security issues
"""

from flask import Flask

# Create Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """Return a simple greeting"""
    return "Hello from CodeArmor Demo"

if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=False, host='127.0.0.1', port=5000)
