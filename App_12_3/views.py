# App_12_3/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'App_12_3/home.html')

def about(request):
    return render(request, 'App_12_3/about.html')

def portfolio(request):
    return render(request, 'App_12_3/portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., save to database, send email)
            # For now, we’ll just display a success message
            messages.success(request, 'Thank you for your message. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'App_12_3/contact.html', {'form': form})
