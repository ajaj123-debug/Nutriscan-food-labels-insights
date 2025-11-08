# 🥗 NutriScan - Food Labels Insights

**NutriScan** is an intelligent web application that uses AI and OCR technology to analyze food product labels, providing detailed nutrition insights and personalized diet plans. Simply scan or upload an image of a food label, and get instant AI-powered analysis of ingredients, health scores, and recommendations.

![NutriScan](https://img.shields.io/badge/NutriScan-AI%20Powered-green) ![Django](https://img.shields.io/badge/Django-5.1.2-092E20?logo=django) ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)

---

## ✨ Features

### 🔍 **Food Label Scanning**
- **Multiple Input Methods**: Upload images or use your device's camera
- **OCR Technology**: Extracts text from food labels using Tesseract OCR
- **Drag & Drop Support**: Easy file upload with drag-and-drop interface
- **Real-time Camera**: Live camera feed for instant scanning

### 🤖 **AI-Powered Analysis**
- **Google Gemini Integration**: Advanced AI analysis of ingredients
- **Health Score**: 1-10 rating system for product healthiness
- **Harmful Ingredient Detection**: Identifies potentially harmful or ultra-processed ingredients
- **Health Concerns**: Detailed list of potential health issues
- **Smart Alternatives**: AI-suggested healthier product alternatives

### 📊 **Nutrition Insights**
- **Comprehensive Reports**: Detailed breakdown of ingredients and their effects
- **Database Matching**: Cross-references with harmful ingredients database
- **Visual Health Score**: Easy-to-understand health rating
- **Summary Analysis**: Quick overview of product healthiness

### 🍽️ **Personalized Diet Plans**
- **6-Day Meal Plans**: Customized meal plans from Monday to Saturday
- **User Profiling**: Considers age, gender, height, weight, activity level, and goals
- **Meal Scheduling**: Breakfast, lunch, dinner, and snacks for each day
- **Calendar Export**: Download diet plan as `.ics` file for calendar apps
- **Goal-Oriented**: Plans tailored to weight loss, muscle gain, maintenance, etc.

### 🎨 **User Experience**
- **Dark Mode Support**: Eye-friendly dark theme
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Modern UI**: Clean, intuitive interface with smooth animations
- **Loading Indicators**: Engaging loading messages during processing

---

## 🛠️ Technology Stack

### Backend
- **Django 5.1.2**: Web framework
- **Python 3.10+**: Programming language
- **SQLite**: Database (default)
- **Tesseract OCR**: Text extraction from images
- **Google Gemini AI**: AI-powered analysis

### Frontend
- **HTML5/CSS3**: Modern web standards
- **JavaScript/jQuery**: Interactive UI
- **Responsive Design**: Mobile-first approach

### Deployment
- **Docker**: Containerization support
- **Gunicorn**: Production WSGI server
- **WhiteNoise**: Static file serving

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **Tesseract OCR** ([Installation Guide](https://github.com/tesseract-ocr/tesseract))
  - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
  - **macOS**: `brew install tesseract`
  - **Linux**: `sudo apt-get install tesseract-ocr`
- **pip**: Python package manager
- **Git**: Version control (optional)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Nutriscan-food-labels-insights.git
cd Nutriscan-food-labels-insights
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## ⚙️ Configuration

### Google Gemini API Key

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Update the API key in `ocr_app_pr1/gemini.py`:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

**⚠️ Security Note**: For production, use environment variables instead of hardcoding:

```python
import os
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
```

### Django Settings

Update `ocr_project_pr1/settings.py` if needed:

- **SECRET_KEY**: Generate a new secret key for production
- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Add your domain name
- **DATABASES**: Configure PostgreSQL/MySQL for production

### Tesseract OCR Path

The application automatically detects Tesseract. If needed, manually set the path in `ocr_app_pr1/views.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# or
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Linux/macOS
```

---

## 🎯 Usage

### Running the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

### Using the Application

#### 1. **Scan a Food Label**
   - Navigate to the home page
   - Click "Scan a Product Now"
   - Choose between:
     - **Upload Image**: Drag & drop or browse for an image
     - **Use Camera**: Take a photo with your device camera
   - Click "Analyze" to process the image

#### 2. **View Analysis Results**
   - Health score (1-10)
   - List of harmful ingredients
   - Health concerns
   - Suggested alternatives
   - Full AI analysis summary

#### 3. **Generate a Diet Plan**
   - Click "Create Your Plan" from the home page
   - Fill in your details:
     - Age
     - Gender
     - Height (cm)
     - Weight (kg)
     - Activity Level
     - Goal (weight loss, muscle gain, etc.)
   - Click "Generate Plan"
   - Download as calendar file (optional)

---

## 📁 Project Structure

```
Nutriscan-food-labels-insights/
│
├── ocr_app_pr1/              # Main Django app
│   ├── models.py             # Database models (HarmfulIngredient)
│   ├── views.py              # View functions (scanning, diet plan)
│   ├── gemini.py             # Google Gemini AI integration
│   ├── admin.py              # Django admin configuration
│   ├── templates/            # HTML templates
│   │   ├── base.html
│   │   ├── Home.html
│   │   ├── index.html        # Scan page
│   │   ├── Ingredient.html   # Results page
│   │   ├── diet_plan.html
│   │   └── ...
│   └── static/               # Static files (CSS, images)
│
├── ocr_project_pr1/          # Django project settings
│   ├── settings.py           # Django configuration
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI configuration
│
├── staticfiles/              # Collected static files
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
└── README.md                 # This file
```

---

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t nutriscan .
```

### Run the Container

```bash
docker run -p 8000:8000 nutriscan
```

The application will be available at `http://localhost:8000`.

### Docker Compose (Optional)

Create a `docker-compose.yml`:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=your_api_key_here
    volumes:
      - .:/app
```

Run with:
```bash
docker-compose up
```

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/upload_and_scan_image` | GET/POST | Scan and analyze food label |
| `/Ingredient` | GET | Display analysis results |
| `/diet_plan` | GET/POST | Generate personalized diet plan |
| `/generate-calendar` | GET | Download diet plan as ICS file |
| `/About` | GET | About page |
| `/Contact` | GET | Contact page |
| `/admin/` | GET | Django admin panel |

---

## 🔧 Development

### Adding Harmful Ingredients to Database

1. Access Django admin: `http://127.0.0.1:8000/admin/`
2. Navigate to "Harmful Ingredients"
3. Add new ingredients with names and descriptions

Or use Django shell:

```bash
python manage.py shell
```

```python
from ocr_app_pr1.models import HarmfulIngredient

HarmfulIngredient.objects.create(
    name="High Fructose Corn Syrup",
    description="Linked to obesity and metabolic issues."
)
```

### Running Tests

```bash
python manage.py test
```

---

## 🚢 Production Deployment

### Recommended Settings

1. **Use Environment Variables**:
   ```python
   SECRET_KEY = os.getenv('SECRET_KEY')
   DEBUG = os.getenv('DEBUG', 'False') == 'True'
   ```

2. **Use PostgreSQL**:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nutriscan_db',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Configure Static Files**:
   - Use WhiteNoise (already configured)
   - Or use a CDN like AWS S3

4. **Security**:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use HTTPS
   - Set secure cookies

### Deploy to Render/Heroku

1. Create `Procfile`:
   ```
   web: gunicorn ocr_project_pr1.wsgi:application
   ```

2. Set environment variables in your hosting platform
3. Deploy!

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **Tesseract OCR**: For text extraction capabilities
- **Google Gemini**: For AI-powered analysis
- **Django Community**: For the excellent web framework

---

## 📞 Support

For issues, questions, or contributions:

- **GitHub Issues**: [Open an issue](https://github.com/ajaj123-debug/Nutriscan-food-labels-insights/issues)
- **Email**: your-email@example.com

---

## 🎯 Roadmap

- [ ] Multi-language support
- [ ] Barcode scanning integration
- [ ] Nutrition facts table extraction
- [ ] User accounts and history
- [ ] Mobile app (React Native)
- [ ] Recipe suggestions based on scanned products
- [ ] Allergen detection and warnings
- [ ] Integration with fitness trackers

---

## ⚠️ Disclaimer

NutriScan provides AI-generated analysis and recommendations. Always consult with healthcare professionals or registered dietitians for personalized medical or nutritional advice. The health scores and ingredient analysis are for informational purposes only.

---

**Made with ❤️ for healthier food choices**