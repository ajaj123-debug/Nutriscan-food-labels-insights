#!/usr/bin/env python3
"""
Setup script for NutriScan environment configuration
This script helps you set up your .env file with proper environment variables
"""

import os
import secrets
import string
from pathlib import Path


def generate_secret_key():
    """Generate a secure Django secret key"""
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(50))


def create_env_file():
    """Create a .env file with proper configuration"""
    env_content = f"""# Environment Configuration for NutriScan
# Generated automatically - DO NOT commit this file to version control

# Environment (development, staging, production)
ENVIRONMENT=development

# Django Secret Key (generated automatically)
SECRET_KEY={generate_secret_key()}

# Google OAuth2 Credentials
# Replace these with your actual Google OAuth2 credentials
GOOGLE_OAUTH2_KEY=your-google-oauth2-client-id-here
GOOGLE_OAUTH2_SECRET=your-google-oauth2-client-secret-here

# Database Configuration (for production)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Email Configuration (for production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Cache Configuration (for production)
# REDIS_URL=redis://localhost:6379/0

# Static Files (for production)
# AWS_ACCESS_KEY_ID=your-aws-access-key
# AWS_SECRET_ACCESS_KEY=your-aws-secret-key
# AWS_STORAGE_BUCKET_NAME=your-bucket-name
# AWS_S3_REGION_NAME=your-region
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ .env file created successfully!")
    print("⚠️  IMPORTANT: Update the Google OAuth2 credentials in the .env file")
    print("⚠️  IMPORTANT: Never commit the .env file to version control")


def main():
    """Main setup function"""
    print("🚀 NutriScan Environment Setup")
    print("=" * 40)
    
    if os.path.exists('.env'):
        response = input("⚠️  .env file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    create_env_file()
    
    print("\n📋 Next steps:")
    print("1. Update GOOGLE_OAUTH2_KEY and GOOGLE_OAUTH2_SECRET in .env")
    print("2. For production, set ENVIRONMENT=production")
    print("3. Configure your database settings if needed")
    print("4. Run: python manage.py runserver")
    
    print("\n🔒 Security reminder:")
    print("- Never commit .env file to git")
    print("- Use different credentials for development and production")
    print("- Regularly rotate your secret keys")


if __name__ == "__main__":
    main()
