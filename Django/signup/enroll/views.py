
from django.shortcuts import render, HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from  .forms import EditAdminUserProfileForm, SingupForm,EditUserProfileForm
from django.contrib import messages

# Create your views here.
# def sign_up(request):
#     if request.method =="POST":
#         fm=UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:

#         fm = UserCreationForm()
#     return render(request,'enroll/signup.html',{'form':fm})


#Signup view function
def sign_up(request):
    if request.method =="POST":
        fm=SingupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully !!')
            fm.save()
    else:



        fm = SingupForm()
    return render(request,'enroll/signup.html',{'form':fm})

#login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass =fm.cleaned_data['password']
                user =authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'logged in Successfully !!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
     return HttpResponseRedirect('/profile/')

#profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser==True:
                 fm=EditUserProfileForm(request.POST,instance=request.user)
            else:
                fm=EditUserProfileForm(request.POST,instance=request.user)     
            if fm.is_valid():
                messages.success(request,'profile updated')
                fm.save()
        else:   
           if  request.user.is_superuser ==True:
            fm =EditAdminUserProfileForm(instance=request.user)
           else:     
            fm = EditUserProfileForm(instance=request.user)  
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')
#logout 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


##change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,"Possword change succesfully !!")
                return HttpResponseRedirect('/profile/')
            else:    
                fm=PasswordChangeForm(user=request.user)
            return render(request,'enroll/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')