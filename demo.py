#!/usr/bin/env python3
"""
Demonstration script for the Vulnerable Python Repository
This shows the vulnerabilities that CodeArmor should detect and fix
"""

def demonstrate_vulnerabilities():
    """Demonstrate the vulnerabilities present in the code"""
    print("=" * 60)
    print("  VULNERABLE PYTHON REPOSITORY - CODEARMOR DEMO")
    print("=" * 60)
    print("⚠️  WARNING: Contains intentional security vulnerabilities")
    print("🎯 Purpose: Test CodeArmor's automated fixing capabilities")
    print("=" * 60)
    
    print("\n🚨 VULNERABILITIES DETECTED:")
    print()
    
    print("1. 🔓 SQL INJECTION (CWE-89) - CRITICAL")
    print("   📄 File: database.py:30")
    print("   💀 Risk: Complete database compromise")
    print("   🔍 Test: curl 'http://localhost:5000/search?username=admin%27%20OR%20%271%27=%271%27%20--'")
    print("   ✅ Fix: Use parameterized queries")
    print()
    
    print("2. 🔑 HARDCODED SECRETS (CWE-798) - HIGH")
    print("   📄 Files: config.py:7-12, main.py:7")
    print("   💀 Risk: Credential exposure in version control")
    print("   🔍 Found: Secret keys, API keys, database credentials")
    print("   ✅ Fix: Move to environment variables")
    print()
    
    print("3. 🧨 UNSAFE YAML LOADING (CWE-502) - CRITICAL")
    print("   📄 File: main.py:22")
    print("   💀 Risk: Remote code execution via deserialization")
    print("   🔍 Test: POST malicious YAML to /config")
    print("   ✅ Fix: Use yaml.safe_load()")
    print()
    
    print("📦 OUTDATED DEPENDENCIES (Multiple CVEs):")
    print("   • Flask 2.0.3 → Should upgrade to 3.x (Security updates)")
    print("   • PyYAML 5.3.1 → Should upgrade to 6.x (CVE-2020-14343)")  
    print("   • requests 2.25.0 → Should upgrade to 2.31.x (CVE-2023-32681)")
    print("   • urllib3 1.26.5 → Should upgrade to 2.x (Multiple CVEs)")
    print()
    
    print("🤖 CODEARMOR EXPECTED ACTIONS:")
    print("   1. 🔧 Auto-fix SQL injection with parameterized queries")
    print("   2. 🔧 Replace hardcoded secrets with env vars")
    print("   3. 🔧 Update Flask framework with compatibility fixes")
    print("   4. 🔧 Upgrade all dependencies to secure versions")
    print("   5. 📝 Create detailed pull request with changes")
    print("   6. 🎫 Generate Jira ticket for sprint tracking")
    print()
    
    print("🚀 TO RUN THE VULNERABLE APP:")
    print("   python main.py")
    print("   Visit: http://localhost:5000")
    print()
    
    print("🧪 TO TEST AFTER FIXES:")
    print("   python test_app.py")
    print()

def main():
    demonstrate_vulnerabilities()

if __name__ == '__main__':
    main()
