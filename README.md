# Vulnerable Python App for CodeArmor Testing

This repository contains **intentional vulnerabilities** designed to test CodeArmor's AI-driven vulnerability fixing capabilities.

## 🚨 Vulnerabilities Present (Easy to Fix)

### 1. **Dependency Vulnerabilities** (3 packages)
```
Flask==1.0.2          # CVE-2019-1010083 - Path traversal
requests==2.19.0      # CVE-2018-18074 - SSL verification bypass  
PyYAML==3.13          # CVE-2017-18342 - Arbitrary code execution
```

**AI Fix**: Upgrade to latest versions:
- Flask >= 2.3.0
- requests >= 2.31.0  
- PyYAML >= 6.0

### 2. **Code Vulnerabilities** (3 types)

#### SQL Injection (`database.py`)
```python
# Vulnerable
query = f"SELECT * FROM users WHERE username = '{username}'"

# Fix
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

#### Unsafe YAML Loading (`main.py`)
```python
# Vulnerable  
config = yaml.load(data, Loader=yaml.FullLoader)

# Fix
config = yaml.safe_load(data)
```

#### Hardcoded Secrets (`config.py`)
```python
# Vulnerable
API_KEY = "sk-1234567890abcdef"

# Fix  
API_KEY = os.getenv('API_KEY')
```

## 🎯 Perfect for AI Testing

- **3 dependency upgrades** (simple version bumps)
- **3 code fixes** (well-documented patterns)
- **Clear before/after examples** provided
- **Automated testing** with GitHub Actions

## 🔧 Files Structure

- `main.py` - Simple Flask app with vulnerabilities
- `database.py` - SQL injection example
- `config.py` - Hardcoded secrets example  
- `requirements_vulnerable.txt` - Outdated dependencies
- `.github/workflows/` - Security scanning workflows

## 🚀 Testing CodeArmor

1. **Detection**: GitHub Security will find all issues
2. **Fix Generation**: AI should generate the fixes shown above
3. **Validation**: Run tests to ensure fixes work
4. **PR Creation**: Generate pull request with changes

**Expected Results**: 6 total fixes (3 dependency + 3 code vulnerabilities)
