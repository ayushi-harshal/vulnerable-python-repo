# Vulnerable Python Web Application for GitHub Security Testing

This is a deliberately vulnerable Python web application designed to trigger GitHub Security alerts and demonstrate CodeArmor's remediation capabilities.

⚠️ **WARNING**: Contains intentional security vulnerabilities for educational purposes only!

## Quick Setup for GitHub Security Testing

1. Create new GitHub repository
2. Copy these files to the new repo
3. Push to GitHub - Security alerts will appear within 24 hours
4. Connect CodeArmor to remediate the issues

## Vulnerabilities Included

- Outdated dependencies with known CVEs
- SQL Injection vulnerabilities  
- Cross-Site Scripting (XSS)
- Command Injection
- Path Traversal
- Unsafe Deserialization
- Hardcoded secrets

## Files

- `vulnerable_web_app.py` - Main vulnerable Flask application
- `requirements_vulnerable.txt` - Dependencies with known vulnerabilities
- `config.py` - Configuration with hardcoded secrets
- `database.py` - SQL injection vulnerabilities
- `utils.py` - Various security issues

## Usage

```bash
# DO NOT run in production!
pip install -r requirements_vulnerable.txt
python vulnerable_web_app.py
```
