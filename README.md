# Vulnerable Python Application for CodeArmor Testing

This repository contains a **deliberately vulnerable** Flask web application designed to test CodeArmor's AI-driven security fixing capabilities.

## 🚨 Security Vulnerabilities Included

### 1. **Hardcoded Secrets** (config.py)
- Database credentials in source code
- API keys hardcoded
- Secret keys not using environment variables

### 2. **SQL Injection** (main.py)
- Direct string concatenation in database queries
- No parameterized queries or input sanitization

### 3. **Command Injection** (main.py)
- User input directly passed to shell commands
- No input validation on system calls

### 4. **Unsafe Deserialization** (main.py)
- Pickle deserialization without validation
- Can lead to remote code execution

### 5. **YAML Code Execution** (main.py)
- Using unsafe YAML loader
- Allows arbitrary code execution

### 6. **Server-Side Template Injection** (main.py)
- Direct template rendering without sanitization
- Template injection vulnerabilities

### 7. **Path Traversal** (main.py)
- No file path validation
- Allows reading arbitrary files

## 📦 Outdated Dependencies

The `requirements_vulnerable.txt` contains intentionally outdated packages:
- Flask 2.0.1 (should be 3.0+)
- PyYAML 5.3.1 (vulnerable version)
- Jinja2 2.11.3 (has template injection issues)
- Various other outdated packages with known CVEs

## 🎯 Purpose

This repository demonstrates:
1. **Vulnerability Detection** - GitHub Security will flag these issues
2. **AI-Powered Fixes** - CodeArmor will generate secure code
3. **Dependency Upgrades** - Framework and library version updates
4. **Automated Testing** - Validation of fixes

## ⚠️ Warning

**DO NOT use this code in production!** This is intentionally vulnerable for testing purposes only.

## 🔧 Expected CodeArmor Fixes

CodeArmor should:
1. Replace hardcoded secrets with environment variables
2. Fix SQL injection with parameterized queries
3. Add input validation and sanitization
4. Replace unsafe deserialization methods
5. Implement secure YAML parsing
6. Add template sanitization
7. Implement path validation
8. Upgrade all dependencies to secure versions
