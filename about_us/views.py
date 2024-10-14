from django.shortcuts import render
from .models import AboutUs

def about_us(request):

    about = AboutUs.objects.all().order_by('order').first()

    return render(request, 'about_us.html', {'about' : about})