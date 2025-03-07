from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pytesseract
from PIL import Image
from .models import HarmfulIngredient  # Import the HarmfulIngredient model
import os
from django.core.files.base import ContentFile
import tempfile

# Set the Tesseract OCR path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import shutil
tesseract_cmd = shutil.which("tesseract")
if tesseract_cmd:
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
else:
    raise RuntimeError("Tesseract OCR not found!")


def upload_and_scan_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        # Create a path in the media directory
        file_name = uploaded_file.name
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
        temp_file.close()
        with open(temp_file_path, 'rb') as image_file:
            extracted_text = pytesseract.image_to_string(Image.open(image_file))


        try:
            # Perform OCR processing on the image
            with default_storage.open(file_path) as image_file:
                extracted_text = pytesseract.image_to_string(Image.open(image_file))

            # Get all harmful ingredients from the database
            harmful_ingredients = HarmfulIngredient.objects.all()
            matched_ingredients = []

            # Check for matches in the extracted text
            for ingredient in harmful_ingredients:
                if ingredient.name.lower() in extracted_text.lower():
                    matched_ingredients.append({'name': ingredient.name, 'description': ingredient.description})

            # Return the matched ingredients as a JSON response
            return JsonResponse({'matched_ingredients': matched_ingredients})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        finally:
            # Delete the file after processing
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

    # If the request method is GET, render the upload form
    return render(request, 'index.html')
def About(request):
    return render(request, 'About.html')
def Contact(request):
    return render(request, 'Contact.html')
def Home(request):
    return render (request, 'Home.html')
def Ingredient(request):
    return render (request, 'Ingredient.html')