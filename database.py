"""
Simple Database Module for CodeArmor Testing
Contains SQL injection vulnerability that's easily fixable
"""

import sqlite3

class UserDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.create_table()
    
    def create_table(self):
        """Create users table"""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def search_user(self, username):
        """VULNERABILITY: SQL Injection (EASY FIX: use parameterized query)"""
        # Vulnerable code - direct string concatenation
        query = f"SELECT * FROM users WHERE username = '{username}'"
        
        cursor = self.conn.execute(query)
        return cursor.fetchall()
    
    def search_user_safe(self, username):
        """FIXED VERSION: Using parameterized queries"""
        # Safe code - parameterized query
        query = "SELECT * FROM users WHERE username = ?"
        cursor = self.conn.execute(query, (username,))
        return cursor.fetchall()
