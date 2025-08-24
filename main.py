"""
Simple Vulnerable Web App for CodeArmor Testing
Contains 3 key vulnerabilities that are easily fixable by AI:
1. SQL Injection
2. Unsafe YAML loading  
3. Hardcoded secrets
"""

from flask import Flask, request
import yaml
import sqlite3

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded secrets (EASY FIX: use environment variables)
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

@app.route('/')
def index():
    return """
    <h1>Simple Vulnerable App for CodeArmor</h1>
    <p>Contains 3 easily fixable vulnerabilities:</p>
    <ul>
        <li><a href="/search?name=test">Search Users (SQL Injection)</a></li>
        <li><a href="/config">Load Config (Unsafe YAML)</a></li>
    </ul>
    """

@app.route('/search')
def search_users():
    """VULNERABILITY 2: SQL Injection (EASY FIX: use parameterized queries)"""
    name = request.args.get('name', '')
    
    # Vulnerable: Direct string concatenation
    query = f"SELECT * FROM users WHERE name = '{name}'"
    
    # Simulate database query
    conn = sqlite3.connect(':memory:')
    try:
        cursor = conn.execute(query)
        return f"Search query: {query}"
    except Exception as e:
        return f"Query failed: {e}"
    finally:
        conn.close()

@app.route('/config', methods=['POST'])
def load_config():
    """VULNERABILITY 3: Unsafe YAML loading (EASY FIX: use yaml.safe_load)"""
    config_data = request.get_data(as_text=True)
    
    if not config_data:
        config_data = "name: test\nversion: 1.0"
    
    # Vulnerable: Using yaml.load instead of yaml.safe_load
    try:
        config = yaml.load(config_data, Loader=yaml.FullLoader)
        return f"Config loaded: {config}"
    except Exception as e:
        return f"Config error: {e}"

if __name__ == '__main__':
    # Using hardcoded password from above
    print(f"Starting app with DB password: {DATABASE_PASSWORD}")
    app.run(debug=True, host='0.0.0.0')
