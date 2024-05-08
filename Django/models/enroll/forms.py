 
from operator import attrgetter
from tkinter import Widget
from django.core import validators
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):   #modelform 
    class Meta:
        model = Student
        fields = ['stuname','stumail','stupass']
        labels = {'stuname':'Enter Name','stumail':'Enter Mail', 'stupass':'Password'}
        error_messages ={ 'name':{'required':'name must enter'}}
        Widgets ={'stupass':forms.PasswordInput,               # for showing paasword in stars
                'stuname':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Name Here'})


        }




# class StudentRegistration(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # password =forms.CharField(widget=forms.PasswordInput)
    # rpassword =forms.CharField(widget=forms.PasswordInput)
    # # def clean(self):
    #     cleaned_data =super().clean()
    #     valpwd =self.cleaned_data['password']
    #     valrpwd =self.cleaned_data['rpassword']
    #     if valpwd != valrpwd :
    #         raise forms.ValidationError('Password does not match')
    # mobile = forms.IntegerField()
    # agree = forms.BooleanField( label_suffix='',label='I Agree') 
    # def clean_name(self):                           ## for validating single field in form
    #     valname = self.cleaned_data['name']
    #     if len(valname) <5:
    #         raise forms.ValidationError("enter more than or equal to 5 char")
    #         return valname
    # def clean(self):        # validation of complete Django form at once 
    #     cleaned_data = super().clean     # the call to super() clean()ensures that any validation logic in parent classes is maintained
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     valmobile = self.cleaned_data['mobile']
    #     if len(valname) < 4:
    #       raise forms.ValidationError('name should be more than or equal 4')
    #     if len(valemail) < 10:
    #       raise forms.ValidationError('email should be more than or equal 10')
    #     if len(valmobile)<10:
    #       raise forms.ValidationError('name should be  10')
              