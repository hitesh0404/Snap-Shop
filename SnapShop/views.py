from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

from account.models import Carousel
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # response = FileResponse(open(os.path.join(settings.BASE_DIR,'templates/base.html'), 'rb'))
    # return response
    car = Carousel.objects.all()
    print(car)
    context = {
        'cars':car
    }
    return render(request, 'index.html',context)