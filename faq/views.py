from django.shortcuts import render
from .models import FAQ


def faq_list(request):
    faqs = FAQ.objects.order_by('order')
    return render(request, 'faq/list.html', {'faqs': faqs})
    