"""
Configuration file with hardcoded secrets (VULNERABILITY)
These should be moved to environment variables for security
"""

DATABASE_URL = "postgresql://admin:password123@localhost/myapp"

SECRET_KEY = "super-secret-key-that-should-not-be-in-git-12345"

API_KEY = "sk-1234567890abcdef-this-is-a-fake-openai-key"

DEBUG = True

