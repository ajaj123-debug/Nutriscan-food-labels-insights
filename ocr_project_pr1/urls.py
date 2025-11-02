from django.contrib import admin
from django.urls import path
from ocr_app_pr1.views import upload_and_scan_image, diet_plan, generate_calendar
from ocr_app_pr1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('upload_and_scan_image', upload_and_scan_image, name='upload_and_scan_image'),
    path('About', About, name='About'),
    path('Contact', Contact, name='Contact'),
    path('diet_plan', diet_plan, name='diet_plan'),
    path('generate-calendar', generate_calendar, name='generate_calendar'),
    path('scan_result/', scan_result, name='scan_result'),

]