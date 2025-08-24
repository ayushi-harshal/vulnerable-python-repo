from flask import Flask, jsonify, request
import yaml
from database import UserDatabase

# Create Flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardcoded-insecure-key-12345'

# Initialize database
db = UserDatabase()

@app.route('/search')
def search_user():
    username = request.args.get('username', '')
    users = db.search_user(username)
    return jsonify({"users": users})

@app.route('/config', methods=['POST'])
def load_config():
    config_data = request.get_data(as_text=True)
    config = yaml.load(config_data, Loader=yaml.FullLoader)
    return jsonify({"config": config})

@app.route('/')
def index():
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
        host='127.0.0.1',  
        port=5000,
        debug=False
    )
