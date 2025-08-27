# NutriScan Deployment Guide

This guide explains how to configure your NutriScan application for different environments (development, staging, production).

## 🏗️ Environment-Based Configuration

Your application now supports different configurations based on the `ENVIRONMENT` variable:

- **Development**: `ENVIRONMENT=development` (default)
- **Staging**: `ENVIRONMENT=staging`
- **Production**: `ENVIRONMENT=production`

## 🚀 Quick Setup

### 1. Initial Setup
```bash
# Run the setup script to create your .env file
python setup_environment.py
```

### 2. Configure Environment Variables
Edit your `.env` file with your actual credentials:

```env
# Environment
ENVIRONMENT=development

# Django Secret Key (auto-generated)
SECRET_KEY=your-generated-secret-key

# Google OAuth2 Credentials
GOOGLE_OAUTH2_KEY=your-actual-google-oauth2-client-id
GOOGLE_OAUTH2_SECRET=your-actual-google-oauth2-client-secret
```

### 3. Generate Secret Key (Alternative)
```bash
python manage.py generate_secret_key
```

## 🔧 Environment-Specific Configurations

### Development Environment
- **DEBUG**: `True`
- **Database**: SQLite
- **Static Files**: Local storage
- **Logging**: Verbose (DEBUG level)
- **Security**: Basic settings
- **Allowed Hosts**: localhost, 127.0.0.1, 0.0.0.0

### Production Environment
- **DEBUG**: `False`
- **Database**: PostgreSQL (recommended)
- **Static Files**: Compressed with WhiteNoise
- **Logging**: WARNING level only
- **Security**: Enhanced (HTTPS, HSTS, etc.)
- **Allowed Hosts**: Your production domain only

## 🌐 Deployment Platforms

### Render.com
1. Set environment variables in Render dashboard:
   ```
   ENVIRONMENT=production
   SECRET_KEY=your-production-secret-key
   GOOGLE_OAUTH2_KEY=your-production-oauth-key
   GOOGLE_OAUTH2_SECRET=your-production-oauth-secret
   ```

2. Your `render.yaml` should reference these environment variables

### Heroku
1. Set environment variables:
   ```bash
   heroku config:set ENVIRONMENT=production
   heroku config:set SECRET_KEY=your-production-secret-key
   heroku config:set GOOGLE_OAUTH2_KEY=your-production-oauth-key
   heroku config:set GOOGLE_OAUTH2_SECRET=your-production-oauth-secret
   ```

### Local Development
1. Use the `.env` file (already in `.gitignore`)
2. Set `ENVIRONMENT=development`
3. Use development OAuth credentials

## 🔒 Security Best Practices

### 1. Never Commit Secrets
- ✅ `.env` file is in `.gitignore`
- ✅ Use environment variables for all secrets
- ✅ Different credentials for each environment

### 2. OAuth Configuration
- **Development**: Use localhost redirect URIs
- **Production**: Use your production domain redirect URIs
- **Staging**: Use staging domain redirect URIs

### 3. Database Security
- **Development**: SQLite (file-based)
- **Production**: PostgreSQL with proper authentication
- **Staging**: Separate database instance

## 📁 File Structure
```
your-project/
├── .env                    # Local environment variables (gitignored)
├── env.example            # Example environment file
├── setup_environment.py   # Setup script
├── ocr_project_pr1/
│   └── settings.py        # Environment-aware settings
└── ocr_app_pr1/
    └── management/
        └── commands/
            └── generate_secret_key.py
```

## 🚨 Troubleshooting

### GitHub Push Protection
If GitHub blocks your push due to secrets:
1. Remove hardcoded secrets from your code
2. Use environment variables instead
3. Update your `.env` file with the actual values
4. Commit the changes without the `.env` file

### OAuth Errors
- Check redirect URIs match your environment
- Verify OAuth credentials are correct
- Ensure environment variables are set properly

### Database Issues
- Development: Check SQLite file permissions
- Production: Verify database connection strings
- Ensure migrations are applied

## 🔄 Environment Switching

To switch between environments:

1. **Development**:
   ```bash
   export ENVIRONMENT=development
   python manage.py runserver
   ```

2. **Production**:
   ```bash
   export ENVIRONMENT=production
   python manage.py collectstatic
   python manage.py runserver
   ```

3. **Using .env file**:
   ```bash
   # Edit .env file
   ENVIRONMENT=production
   # Then run your Django commands
   ```

## 📊 Monitoring

### Development Logging
- Full debug information
- SQL queries logged
- OAuth debugging enabled

### Production Logging
- WARNING level and above only
- No sensitive information logged
- Structured logging format

## 🎯 Next Steps

1. Set up your `.env` file with proper credentials
2. Test the application in development mode
3. Configure your production environment variables
4. Deploy to your chosen platform
5. Monitor logs and performance

## 📞 Support

If you encounter issues:
1. Check the environment variables are set correctly
2. Verify OAuth credentials and redirect URIs
3. Review the Django logs for error messages
4. Ensure all required packages are installed
