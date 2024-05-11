from django.shortcuts import render,HttpResponseRedirect
from .forms import SingupForm, LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import Group
from .models import Post
# Create your views here.
#Home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
#About
def about(request):
    return render(request,'blog/about.html')    

# contact
def contact(request):
    return render(request,'blog/contact.html')  

# deshboard
def deshboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()

        return render(request,'blog/deshboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
       return HttpResponseRedirect('/login/') 


# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

    


# signup
def signup(request):
    if request.method=="POST":
      form = SingupForm(request.POST) 
      if form.is_valid():
          messages.success(request,'Congratulation!! you have become an author.')

          user=form.save()
          group=Group.objects.get(name='Author')
          user.groups.add(group)
    else:

     form= SingupForm()

    return render(request,'blog/signup.html',{'form':form})
            
# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname =form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user  = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully')
                    return HttpResponseRedirect('/deshboard/')
                
                
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
            
    else:
      return HttpResponseRedirect('/deshboard/')

#Add New Post
def add_post(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PostForm(request.POST)
            if form.is_valid():
               title =form.cleaned_data['title']
               desc =form.cleaned_data['desc']
               pst=Post(title=title,desc=desc)
               pst.save()
               form=PostForm()
               messages.success(request,'Post added Successfully !!!!')
               

        else:    
            form=PostForm()
        return render(request,'blog/addpost.html' ,{'form':form})
    else:
     return HttpResponseRedirect('/login/')
 

# Update Post

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                
                
                messages.success(request,'Post Updated Sucessfully !!!')
        else:
          pi=Post.objects.get(pk=id)
          form=PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')








# Delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            
            messages.success(request,f"Post {id} deleted successfully")
            return HttpResponseRedirect('/deshboard/')
    else:
        return HttpResponseRedirect('/login/')
    
