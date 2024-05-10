
from cProfile import label
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# for extend the class means we need to add our own fields in the signup forms like last name, first name, email
class SingupForm(UserCreationForm):
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput) # if we want to change label of password field then we will change it from Usercreationform class.
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels ={'email':"Email"}

class EditUserProfileForm(UserChangeForm):
    password = None 
    class Meta:
        model= User
        fields =['username','first_name','last_name','email','date_joined','last_login']
        label={'email':'Email'}        


class EditAdminUserProfileForm(UserChangeForm):
    password = None 
    class Meta:
        model= User
        fields ="__all__"
        label={'email':'Email'}        