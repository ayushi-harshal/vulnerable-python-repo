"""
Configuration file with hardcoded secrets and insecure settings
"""

import os

# VULNERABILITY: Hardcoded secrets in configuration
SECRET_KEY = "supersecretkey123456789"
DATABASE_PASSWORD = "admin123"
JWT_SECRET = "jwtsecret2023"
ENCRYPTION_KEY = "encryptionkey12345"

# VULNERABILITY: Hardcoded API keys
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuv"
AWS_ACCESS_KEY_ID = "AKIA1234567890ABCDEF"
AWS_SECRET_ACCESS_KEY = "abcdefghijklmnopqrstuvwxyz1234567890ABC"
OPENAI_API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyzABCDEF"

# VULNERABILITY: Database connection with hardcoded credentials
DATABASE_CONFIG = {
    'host': 'production-db.company.com',
    'port': 5432,
    'database': 'prod_app',
    'username': 'dbadmin',
    'password': 'dbpassword123',
    'ssl_mode': 'disable'  # Insecure SSL configuration
}

# VULNERABILITY: Insecure configuration settings
DEBUG = True  # Debug mode enabled in production
TESTING = True
ALLOWED_HOSTS = ['*']  # Allows any host - security risk

# VULNERABILITY: Insecure session configuration
SESSION_CONFIG = {
    'secure': False,  # Session cookies not marked as secure
    'httponly': False,  # Session cookies accessible via JavaScript
    'samesite': None,  # No SameSite protection
    'permanent_session_lifetime': 86400 * 365  # 1 year session lifetime
}

# VULNERABILITY: Weak CORS configuration
CORS_CONFIG = {
    'origins': ['*'],  # Allows requests from any origin
    'methods': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    'allow_credentials': True,
    'max_age': 86400
}

# VULNERABILITY: File upload configuration - no restrictions
UPLOAD_CONFIG = {
    'max_file_size': 100 * 1024 * 1024,  # 100MB - too large
    'allowed_extensions': ['*'],  # All file types allowed
    'upload_path': '/tmp/uploads',  # Insecure upload path
    'virus_scan': False,  # No virus scanning
    'execute_uploaded_files': True  # Dangerous - allows execution
}

# VULNERABILITY: Logging configuration that might log sensitive data
LOGGING_CONFIG = {
    'level': 'DEBUG',
    'log_passwords': True,  # Logs passwords
    'log_api_keys': True,  # Logs API keys
    'log_sql_queries': True,  # Logs SQL queries (might contain sensitive data)
    'log_file': '/tmp/app.log',  # World-readable log location
    'log_remote': True,
    'remote_log_server': 'log-server.company.com:514'
}

# VULNERABILITY: External service configuration with insecure settings
REDIS_CONFIG = {
    'host': 'redis.company.com',
    'port': 6379,
    'password': None,  # No authentication
    'ssl': False,  # No encryption
    'db': 0
}

ELASTICSEARCH_CONFIG = {
    'host': 'elastic.company.com',
    'port': 9200,
    'use_ssl': False,  # No encryption
    'verify_certs': False,  # SSL certificate verification disabled
    'username': None,  # No authentication
    'password': None
}

# VULNERABILITY: Email configuration with plaintext credentials
EMAIL_CONFIG = {
    'smtp_server': 'smtp.company.com',
    'smtp_port': 25,  # Unencrypted SMTP
    'username': 'noreply@company.com',
    'password': 'emailpassword123',  # Hardcoded password
    'use_tls': False,  # No encryption
    'use_ssl': False
}

# VULNERABILITY: Third-party integrations with weak security
THIRD_PARTY_APIS = {
    'payment_processor': {
        'api_key': 'pk_test_1234567890abcdef',
        'secret_key': 'sk_test_abcdef1234567890',
        'webhook_secret': 'whsec_1234567890abcdef',
        'sandbox_mode': False  # Production keys in code
    },
    'analytics': {
        'tracking_id': 'UA-123456789-1',
        'api_secret': 'analytics_secret_123'
    }
}

# VULNERABILITY: Admin credentials in configuration
ADMIN_USERS = {
    'admin': 'admin123',
    'root': 'password',
    'administrator': 'admin',
    'test': 'test123'
}

# VULNERABILITY: Crypto configuration with weak algorithms
CRYPTO_CONFIG = {
    'algorithm': 'MD5',  # Weak hashing algorithm
    'encryption_algorithm': 'DES',  # Weak encryption
    'key_length': 56,  # Too short
    'salt_length': 4,  # Too short
    'iterations': 1000  # Too few iterations for PBKDF2
}

def get_secret_key():
    """Returns hardcoded secret key - vulnerability"""
    return SECRET_KEY

def get_database_url():
    """Constructs database URL with hardcoded credentials"""
    config = DATABASE_CONFIG
    return f"postgresql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

def is_debug_enabled():
    """Returns debug status"""
    return DEBUG or os.environ.get('DEBUG', '').lower() == 'true'
