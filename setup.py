#!/usr/bin/env python3
"""
Setup script for Instagram Keyword Scraper

This script helps set up the environment and verify the installation.
"""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required.")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True


def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False


def setup_environment():
    """Set up environment file."""
    env_file = Path(".env")
    env_example = Path("env.example")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    if not env_example.exists():
        print("❌ env.example file not found")
        return False
    
    # Copy env.example to .env
    try:
        with open(env_example, 'r') as src, open(env_file, 'w') as dst:
            dst.write(src.read())
        print("✅ Created .env file from env.example")
        print("⚠️  Please edit .env and add your Apify API token")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False


def create_output_directory():
    """Create output directory for results."""
    output_dir = Path("output")
    try:
        output_dir.mkdir(exist_ok=True)
        print("✅ Output directory created")
        return True
    except Exception as e:
        print(f"❌ Failed to create output directory: {e}")
        return False


def verify_apify_token():
    """Check if Apify token is configured."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        token = os.getenv('APIFY_API_TOKEN')
        if not token or token == 'your_apify_api_token_here':
            print("⚠️  Apify API token not configured in .env file")
            print("   Please edit .env and add your token from https://console.apify.com/account/integrations")
            return False
        
        print("✅ Apify API token configured")
        return True
    except ImportError:
        print("❌ python-dotenv not installed")
        return False


def test_imports():
    """Test if all required modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        import apify_client
        print("✅ apify-client imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import apify-client: {e}")
        return False
    
    try:
        import pandas
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import pandas: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import python-dotenv: {e}")
        return False
    
    return True


def main():
    """Main setup function."""
    print("🚀 Instagram Keyword Scraper - Setup")
    print("=" * 40)
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
    
    # Install requirements
    if not install_requirements():
        success = False
    
    # Set up environment
    if not setup_environment():
        success = False
    
    # Create output directory
    if not create_output_directory():
        success = False
    
    # Test imports
    if not test_imports():
        success = False
    
    # Check Apify token
    verify_apify_token()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Edit .env file and add your Apify API token")
        print("2. Run: python instagram_scraper.py")
        print("3. Or run: python examples.py")
    else:
        print("❌ Setup encountered errors. Please fix them and try again.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
