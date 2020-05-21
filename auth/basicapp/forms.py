from django import forms
from django.contrib.auth.models import User
from . models import profile

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']
class UserProfile(forms.ModelForm):
    class Meta:
        model=profile
        fields=['user_url','profile_pic']
