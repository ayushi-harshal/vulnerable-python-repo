"""
Database module with SQL injection vulnerabilities
"""

import sqlite3
import hashlib
import os

# VULNERABILITY: Hardcoded database credentials
DB_HOST = "localhost"
DB_USER = "admin"
DB_PASS = "password123"
DB_NAME = "vulnerable_app"

class DatabaseManager:
    def __init__(self):
        # VULNERABILITY: Using SQLite without proper configuration
        self.conn = sqlite3.connect('vulnerable_app.db', check_same_thread=False)
        self.setup_tables()
    
    def setup_tables(self):
        """Setup database tables"""
        cursor = self.conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                email TEXT,
                role TEXT DEFAULT 'user'
            )
        ''')
        
        # Insert some test data
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password, email, role) 
            VALUES ('admin', 'admin123', 'admin@example.com', 'admin')
        ''')
        
        self.conn.commit()
    
    def authenticate_user(self, username, password):
        """VULNERABILITY: SQL Injection in authentication"""
        cursor = self.conn.cursor()
        
        # Direct string concatenation - SQL injection vulnerability
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        cursor.execute(query)
        return cursor.fetchone()
    
    def search_users(self, search_term):
        """VULNERABILITY: SQL Injection in search"""
        cursor = self.conn.cursor()
        
        # No parameterized queries - SQL injection vulnerability
        query = f"SELECT username, email FROM users WHERE username LIKE '%{search_term}%' OR email LIKE '%{search_term}%'"
        
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_user_by_id(self, user_id):
        """VULNERABILITY: SQL Injection via user_id"""
        cursor = self.conn.cursor()
        
        # Assuming user_id comes from user input without validation
        query = f"SELECT * FROM users WHERE id = {user_id}"
        
        cursor.execute(query)
        return cursor.fetchone()
    
    def update_user_email(self, username, new_email):
        """VULNERABILITY: SQL Injection in update"""
        cursor = self.conn.cursor()
        
        # Direct string formatting - SQL injection vulnerability
        query = f"UPDATE users SET email = '{new_email}' WHERE username = '{username}'"
        
        cursor.execute(query)
        self.conn.commit()
        return cursor.rowcount
    
    def delete_user(self, username):
        """VULNERABILITY: SQL Injection in delete"""
        cursor = self.conn.cursor()
        
        # No input validation - SQL injection vulnerability
        query = f"DELETE FROM users WHERE username = '{username}'"
        
        cursor.execute(query)
        self.conn.commit()
        return cursor.rowcount
    
    def get_user_orders(self, username, order_by):
        """VULNERABILITY: SQL Injection via ORDER BY"""
        cursor = self.conn.cursor()
        
        # User-controlled ORDER BY clause - SQL injection vulnerability
        query = f"SELECT * FROM orders WHERE username = '{username}' ORDER BY {order_by}"
        
        cursor.execute(query)
        return cursor.fetchall()
    
    def backup_database(self, backup_path):
        """VULNERABILITY: Path traversal in backup"""
        # No path validation - path traversal vulnerability
        os.system(f"cp vulnerable_app.db {backup_path}")
    
    def hash_password(self, password):
        """VULNERABILITY: Weak password hashing"""
        # Using weak MD5 instead of bcrypt/scrypt/argon2
        return hashlib.md5(password.encode()).hexdigest()
    
    def log_query(self, query):
        """VULNERABILITY: Information disclosure in logs"""
        # Logging sensitive queries without sanitization
        with open('/tmp/query.log', 'a') as f:
            f.write(f"QUERY: {query}\n")

# Global database instance - potential race conditions
db = DatabaseManager()
