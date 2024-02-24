from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
    
    
 
 