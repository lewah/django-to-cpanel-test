from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'form/home.html')
