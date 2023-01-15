from django.shortcuts import render
from .forms import EnrollmentForm # import the form from forms.py
# Create your views here.

def form(request):
    context = {
        'form': EnrollmentForm() # pass form into the context
    }
    return render(request, 'index.html', context) 
