# Vulnerable Python App for CodeArmor Testing

This repository contains **intentional vulnerabilities** designed to test CodeArmor's AI-driven vulnerability fixing capabilities.

## 🚨 Vulnerabilities Present (6 Total - Easy to Fix)

### **Dependency Vulnerabilities** (3 packages)
```
Flask==1.0.2          # CVE-2019-1010083 - Path traversal
requests==2.19.0      # CVE-2018-18074 - SSL verification bypass  
PyYAML==3.13          # CVE-2017-18342 - Arbitrary code execution
```

**AI Fix**: Upgrade to latest secure versions:
- Flask >= 3.0.0
- requests >= 2.31.0  
- PyYAML >= 6.0

### **Code Vulnerabilities** (3 types)

#### 1. SQL Injection (`database.py`)
```python
# Vulnerable
query = f"SELECT * FROM users WHERE username = '{username}'"

# Fix
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

#### 2. Unsafe YAML Loading (`main.py`)
```python
# Vulnerable  
config = yaml.load(data, Loader=yaml.FullLoader)

# Fix
config = yaml.safe_load(data)
```

#### 3. Hardcoded Secrets (`config.py` & `main.py`)
```python
# Vulnerable
SECRET_KEY = "hardcoded-insecure-key-12345"

# Fix  
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-only')
```

## 🎯 Perfect for AI Testing

- **3 dependency upgrades** (simple version bumps)
- **3 code fixes** (well-documented patterns)
- **Clear before/after examples** provided
- **GitHub Security integration** for detection
- **Automated CI/CD** with security scanning

## 🔧 Files Structure

```
├── main.py                     # Flask app with hardcoded secrets & YAML vuln
├── database.py                 # SQL injection example
├── config.py                   # Hardcoded secrets example  
├── requirements_vulnerable.txt # Outdated dependencies
└── .github/workflows/          # Security scanning (CodeQL, Bandit)
```

## 🚀 Testing CodeArmor

1. **Detection**: GitHub Security will automatically find all 6 issues
2. **Fix Generation**: AI should generate the secure code patterns shown above
3. **Validation**: Automated tests verify fixes work correctly
4. **PR Creation**: Generate pull request with detailed change descriptions
5. **Jira Integration**: Create tickets for sprint tracking

**Expected Results**: 6 total fixes (3 dependency upgrades + 3 code vulnerabilities)

---

⚠️ **WARNING**: This code is intentionally vulnerable. Do NOT use in production!
