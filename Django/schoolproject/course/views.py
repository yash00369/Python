
from django.shortcuts import render
from django.http import HttpResponse


"""
 Create your views here.
 def index(request):
     return HttpResponse(" home page")

 def learn_django(request):
     return HttpResponse("<h1>hello Django</h1>")
 def learn_python(request):
     return HttpResponse("<h1>hello python</h1>") 
"""

#####for render the template we don't need to http response
def learn_django(request):
    cname="django"
    duration= "4 months"
    seats   = 10
    django_details = {"cn":cname,"du":duration, "st":seats}
    return render(request,"course.html",context=django_details)
def learn_python(request):
    return render(request,"course2.html")    