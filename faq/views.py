from django.shortcuts import render
from .models import FAQ

# Create your views here.
def faq_list(request):
    faqs = FAQ.objects.order_by('order')
    return render(request, 'faq/list.html', {'faqs': faqs})