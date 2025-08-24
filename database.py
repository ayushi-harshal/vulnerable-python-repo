import sqlite3
import os

class UserDatabase:
    def __init__(self):
        self.db_path = 'users.db'
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.create_table()
        self.insert_test_data()
    
    def create_table(self):
        """Create users table if not exists"""
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                role TEXT DEFAULT 'user'
            )
        ''')
        self.conn.commit()
    
    def insert_test_data(self):
        """Insert some test data for demonstration"""
        # Check if data already exists
        cursor = self.conn.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            test_users = [
                ('admin', 'admin@example.com', 'admin'),
                ('john_doe', 'john@example.com', 'user'),
                ('jane_smith', 'jane@example.com', 'user')
            ]
            
            self.conn.executemany(
                "INSERT INTO users (username, email, role) VALUES (?, ?, ?)", 
                test_users
            )
            self.conn.commit()
    
    def search_user(self, username):
        """
        VULNERABILITY: SQL Injection (CWE-89)
        This method is vulnerable to SQL injection attacks
        Example malicious input: admin' OR '1'='1' --
        """
        # VULNERABLE CODE: Direct string concatenation
        query = # Use parameterized queries with ? placeholders
        
        print(f"[VULNERABLE] Executing query: {query}")  # For demonstration
        
        try:
            cursor = self.conn.execute(query)
            results = cursor.fetchall()
            return [{"id": row[0], "username": row[1], "email": row[2], "role": row[3]} for row in results]
        except Exception as e:
            return [{"error": str(e), "query": query}]
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
