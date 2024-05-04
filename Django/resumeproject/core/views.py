from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   context={'home':'active'}
   return render(request, 'home.html',context)
def content(request):
   context={'content':'active'}
   return render(request, 'content.html',context)