"""
Simple Configuration for CodeArmor Testing
Contains hardcoded secrets that need to be moved to environment variables
"""

import os

# VULNERABILITY: Hardcoded secrets (EASY FIX: use environment variables)
DATABASE_URL = "postgresql://admin:password123@localhost/myapp"
SECRET_KEY = "hardcoded-secret-key-123"
API_KEY = "sk-1234567890abcdef"

# FIXED VERSION (commented out - what AI should implement):
# DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')
# SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-only')  
# API_KEY = os.getenv('API_KEY')

DEBUG = True  # Should be False in production
