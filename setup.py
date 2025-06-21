#!/usr/bin/env python3
"""
Setup script for the Student AI Assistant
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file...")
    try:
        with open(".env", "w") as f:
            f.write("# OpenAI API Configuration\n")
            f.write("# Get your API key from: https://platform.openai.com/api-keys\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n\n")
            f.write("# Optional: Customize the AI model\n")
            f.write("# OPENAI_MODEL=gpt-3.5-turbo\n")
            f.write("# OPENAI_TEMPERATURE=0.7\n")
        print("✅ .env file created")
        print("⚠️  Please edit .env file and add your OpenAI API key")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Student AI Assistant...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    print("=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Run: streamlit run app.py")
    print("3. Open your browser to http://localhost:8501")
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main() 