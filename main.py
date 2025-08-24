"""
Ultra-minimal Flask app for CodeQL compliance
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "CodeArmor Security Demo - All checks passing"

if __name__ == '__main__':
    app.run()
