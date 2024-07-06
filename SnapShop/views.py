from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os
def home(request):
    response = FileResponse(open(os.path.join(settings.BASE_DIR,'templates/base.html'), 'rb'))
    return response