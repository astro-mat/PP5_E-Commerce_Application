from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

# class ContactForm(forms.Form):
#     name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     message = forms.CharField(label="Your Message", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))