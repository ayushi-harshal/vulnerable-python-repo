#!/usr/bin/env python3
"""
Setup script for the vulnerable Python repository
This script demonstrates the vulnerabilities before CodeArmor fixes them
"""
import os
import sys
import subprocess

def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("  VULNERABLE PYTHON REPOSITORY - CODEARMOR TESTING")
    print("=" * 60)
    print("⚠️  WARNING: This application contains intentional vulnerabilities")
    print("🎯 Purpose: Testing CodeArmor's automated fixing capabilities")
    print("=" * 60)

def check_requirements():
    """Check if requirements are installed"""
    try:
        import flask
        import yaml
        import requests
        print("✅ All dependencies are installed")
        print(f"📦 Flask version: {flask.__version__}")
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False

def demonstrate_vulnerabilities():
    """Show examples of the vulnerabilities"""
    print("\n VULNERABILITIES PRESENT:")
    print("1. SQL Injection:")
    print("   curl 'http://localhost:5000/search?username=admin%27%20OR%20%271%27=%271%27%20--'")
    
    print("\n2. Unsafe YAML Loading:")
    print("   curl -X POST http://localhost:5000/config -d 'dangerous: !!python/object/apply:os.system [\"echo PWN3D\"]'")
    
    print("\n3. Hardcoded Secrets:")
    print("   Check config.py and main.py for hardcoded credentials")
    
    print("\n4. Outdated Dependencies:")
    print("   Flask 1.0.2 (should be 3.x)")
    print("   PyYAML 5.3.1 (has CVE-2020-14343)")
    print("   requests 2.20.0 (has multiple CVEs)")

def main():
    """Main setup function"""
    print_banner()
    
    if not check_requirements():
        sys.exit(1)
    
    demonstrate_vulnerabilities()
    
    print(f"\n Starting vulnerable Flask application...")
    print("Visit: http://localhost:5000")
    print("Press Ctrl+C to stop")
    
    # Import and run the app
    from main import app
    64     from main import app
65     app.run(host='127.0.0.1', port=5000, debug=False)
66

if __name__ == '__main__':
    main()
