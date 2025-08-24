from flask import Flask, jsonify, request
import yaml
from database import UserDatabase

app = Flask(__name__)
# TODO: Replace with environment variable or secure config

# Initialize database
db = UserDatabase()

@app.route('/search')
def search_user():
    """SQL Injection vulnerable endpoint"""
    username = request.args.get('username', '')
    # VULNERABILITY: This will trigger SQL injection via database.py
    users = db.search_user(username)
    return jsonify({"users": users, "query_username": username})

@app.route('/config', methods=['POST'])
def load_config():
    """Unsafe YAML deserialization endpoint"""
    config_data = request.get_data(as_text=True)
    # VULNERABILITY: Unsafe YAML loading (CWE-502) - allows code execution
    23     # VULNERABILITY: Unsafe YAML loading (CWE-502) - allows code execution
24     config = yaml.safe_load(config_data, Loader=yaml.FullLoader)
25     return jsonify({"config": config, "status": "loaded"})
    return jsonify({"config": config, "status": "loaded"})

@app.route('/')
def index():
    """Application info and vulnerability summary"""
    return jsonify({
        "app": "Vulnerable Flask App for CodeArmor Testing",
        "flask_version": "2.0.3",
        "vulnerabilities": {
            "sql_injection": "GET /search?username=admin' OR 1=1--",
            "yaml_rce": "POST /config with malicious YAML",
            "hardcoded_secrets": "Secret key in source code"
        },
        "framework_issues": {
            "flask": "Outdated 2.0.3 → should upgrade to 3.x",
            "pyyaml": "Vulnerable 5.3.1 → should upgrade to 6.x",
            "requests": "Outdated 2.25.0 → should upgrade to 2.31.x"
        }
    })

if __name__ == '__main__':
    # Run the vulnerable application
    app.run(host='127.0.0.1', port=5000, debug=True)
