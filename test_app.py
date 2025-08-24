#!/usr/bin/env python3
"""
Simple test script to verify the vulnerable Flask app can start
"""

import sys
import requests
import subprocess
import time

def test_app():
    print("Testing vulnerable Flask application...")
    
    try:
        # Start the Flask app in background
        print("Starting Flask app...")
        process = subprocess.Popen([sys.executable, "main.py"], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        
        # Wait a moment for the app to start
        time.sleep(2)
        
        # Test the home endpoint
        print("Testing home endpoint...")
        response = requests.get("http://localhost:5000/", timeout=5)
        print(f"Home endpoint status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Terminate the process
        process.terminate()
        print("Test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Test failed: {e}")
        if 'process' in locals():
            process.terminate()
        return False

if __name__ == "__main__":
    test_app()
