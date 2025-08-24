from setuptools import setup, find_packages

setup(
    name="vulnerable-demo-app",
    version="1.0.0",
    description="Demo Flask application for security testing",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
    ],
    python_requires=">=3.8",
)
