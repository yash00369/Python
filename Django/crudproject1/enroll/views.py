from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import StudentRegistrations
from .models import User
# Create your views here.
# This function will add new item and show All items
def add_show(request):
    if request.method =='POST':
        fm=StudentRegistrations(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)

            reg.save()
            fm =StudentRegistrations()     # after click on add button in form than show blank form
    else:
        fm =StudentRegistrations()
    stud = User.objects.all() #show all the data in template.

    
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

    
# this function will update/Edit
def update_data(request, id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm=StudentRegistrations(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistrations(instance=pi)  

    return render(request,'enroll/update.html',{'form':fm})


    # This function will delete item
def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')