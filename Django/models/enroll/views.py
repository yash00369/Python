from errno import EILSEQ
from django.http import HttpResponseRedirect
from django.shortcuts import render
from enroll.models import Student
from. forms import StudentRegistration
# Create your views here.
def studentinfo(request):
    stud=Student.objects.all()
    return render(request,'enroll/details.html',{'stu':stud})
    
def thankyou(request):
    return render(request, 'enroll/success.html')



def showformdata(request):
    if request.method =="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('name:',fm.cleaned_data['stuname'])
            print('email:',fm.cleaned_data['stumail'])
            print('password:',fm.cleaned_data['stupass'])
            #print('Rpassword:',fm.cleaned_data['rpassword'])
            # print('mobile:',fm.cleaned_data['mobile'])
            #return HttpResponseRedirect('/regi/success/')
    else:
      fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})