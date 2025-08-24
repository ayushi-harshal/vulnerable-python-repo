"""
Utility functions with various security vulnerabilities
"""

import os
import subprocess
import pickle
import yaml
import hashlib
import random
import tempfile
import shutil
import xml.etree.ElementTree as ET

def execute_system_command(command):
    """VULNERABILITY: Command injection via os.system"""
    # Direct execution of user input - command injection
    result = os.system(command)
    return result

def run_shell_command(cmd, use_shell=True):
    """VULNERABILITY: Shell injection in subprocess"""
    # Using shell=True with user input - shell injection
    try:
        output = subprocess.check_output(cmd, shell=use_shell, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def deserialize_user_data(data):
    """VULNERABILITY: Unsafe pickle deserialization"""
    # Deserializing untrusted data - RCE vulnerability
    try:
        return pickle.loads(data)
    except Exception as e:
        return None

def load_yaml_config(yaml_string):
    """VULNERABILITY: Unsafe YAML loading"""
    # Using yaml.load instead of yaml.safe_load - code execution
    try:
        return yaml.load(yaml_string, Loader=yaml.FullLoader)
    except Exception as e:
        return None

def parse_xml_data(xml_string):
    """VULNERABILITY: XML External Entity (XXE) injection"""
    # Parsing XML without disabling external entities
    try:
        root = ET.fromstring(xml_string)
        return root
    except Exception as e:
        return None

def generate_password():
    """VULNERABILITY: Weak random password generation"""
    # Using predictable random for security-critical function
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(8):  # Too short password
        password += random.choice(chars)
    return password

def hash_password(password):
    """VULNERABILITY: Weak password hashing"""
    # Using MD5 without salt - vulnerable to rainbow tables
    return hashlib.md5(password.encode()).hexdigest()

def create_temp_file(content, suffix=""):
    """VULNERABILITY: Insecure temporary file creation"""
    # Creating temp files with predictable names
    temp_name = f"/tmp/app_temp_{random.randint(1000, 9999)}{suffix}"
    
    with open(temp_name, 'w') as f:
        f.write(content)
    
    # Setting world-readable permissions
    os.chmod(temp_name, 0o777)
    return temp_name

def read_file_contents(file_path):
    """VULNERABILITY: Path traversal vulnerability"""
    # No validation of file path - directory traversal
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_user_file(filename, content):
    """VULNERABILITY: Path traversal in file write"""
    # User-controlled filename without validation
    file_path = f"/uploads/{filename}"
    
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        return False

def backup_files(source_dir, backup_name):
    """VULNERABILITY: Command injection in backup"""
    # Using user input in shell command
    backup_cmd = f"tar -czf {backup_name}.tar.gz {source_dir}"
    return os.system(backup_cmd)

def download_file(url, filename):
    """VULNERABILITY: Server-Side Request Forgery (SSRF)"""
    # No URL validation - SSRF vulnerability
    import urllib.request
    
    try:
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        return False

def eval_expression(expression):
    """VULNERABILITY: Code injection via eval"""
    # Direct eval of user input - code injection
    try:
        return eval(expression)
    except Exception as e:
        return None

def exec_code(code_string):
    """VULNERABILITY: Code injection via exec"""
    # Direct exec of user input - code injection
    try:
        exec(code_string)
        return True
    except Exception as e:
        return False

def format_string(template, **kwargs):
    """VULNERABILITY: Format string vulnerability"""
    # Unsafe string formatting - potential information disclosure
    try:
        return template.format(**kwargs)
    except Exception as e:
        return template

def log_sensitive_data(username, password, credit_card):
    """VULNERABILITY: Logging sensitive information"""
    # Logging sensitive data - information disclosure
    log_message = f"User login: {username}, Password: {password}, CC: {credit_card}"
    
    with open('/tmp/app.log', 'a') as f:
        f.write(log_message + '\n')

def generate_session_token():
    """VULNERABILITY: Weak session token generation"""
    # Predictable session token generation
    import time
    token = hashlib.md5(f"{time.time()}_{random.randint(1, 1000)}".encode()).hexdigest()
    return token

def validate_user_input(user_input):
    """VULNERABILITY: Insufficient input validation"""
    # Minimal validation - allows dangerous characters
    if len(user_input) > 1000:
        return False
    return True

def sanitize_html(html_content):
    """VULNERABILITY: Incomplete HTML sanitization"""
    # Incomplete sanitization - XSS vulnerability
    dangerous_tags = ['script', 'iframe']
    
    for tag in dangerous_tags:
        html_content = html_content.replace(f'<{tag}', f'&lt;{tag}')
    
    return html_content

def encrypt_data(data, key="default_key"):
    """VULNERABILITY: Weak encryption implementation"""
    # Simple XOR "encryption" - not secure
    encrypted = ""
    for i, char in enumerate(data):
        encrypted += chr(ord(char) ^ ord(key[i % len(key)]))
    return encrypted

def decrypt_data(encrypted_data, key="default_key"):
    """VULNERABILITY: Same weak encryption for decryption"""
    # Using same weak XOR method
    return encrypt_data(encrypted_data, key)  # XOR is symmetric

def check_file_extension(filename):
    """VULNERABILITY: Insufficient file type validation"""
    # Only checking extension, not content
    allowed_extensions = ['.txt', '.jpg', '.png', '.pdf']
    
    for ext in allowed_extensions:
        if filename.endswith(ext):
            return True
    return False

def compress_file(input_file, output_file):
    """VULNERABILITY: Zip slip vulnerability"""
    # No path validation in zip operations
    import zipfile
    
    with zipfile.ZipFile(output_file, 'w') as zipf:
        zipf.write(input_file)
    
    return True

def extract_archive(archive_path, extract_to):
    """VULNERABILITY: Zip slip during extraction"""
    import zipfile
    
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        # No path validation during extraction - zip slip vulnerability
        zipf.extractall(extract_to)
    
    return True
