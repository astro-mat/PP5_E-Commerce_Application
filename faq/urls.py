from django.urls import path
from .views import faq_list

urlpatterns = [
    # ... other URL patterns ...
    path('faq/', faq_list, name='faq_list'),
]