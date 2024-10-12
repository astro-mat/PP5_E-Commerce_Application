from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f'Contact Form Submission - {name}'
            body = f'From: {name}\nEmail: {email}\nMessage:\n{message}'

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # Send confirmation email to user
            user_email = contact.email
            user_message = f"""
            Dear {contact.name},

            Thank you for contacting us. We have received your message and will respond soon.

            Details of your submission:
            Name: {contact.name}
            Email: {contact.email}
            Message: {contact.message}

            Our team will review your inquiry and get back to you shortly.

            Best regards,
            [Your Company Name]
            """
            send_mail(
                'Thank you for your message',
                user_message,
                settings.EMAIL_HOST_USER,
                [user_email],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')