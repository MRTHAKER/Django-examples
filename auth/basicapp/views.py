from django.shortcuts import render
from basicapp.forms import UserForm,UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(req):
    return render(req,'basicapp/index.html')

@login_required
def logout_user(req):
    logout(req)
    return HttpResponseRedirect(reverse('basicapp:index'))


@login_required
def dashboard(req):
    return HttpResponse('You are logged in')

def register(req):
    registered=False
    if( req.method == 'POST'):
        userform=UserForm(data=req.POST)
        profileform=UserProfile(data=req.POST)
        if(userform.is_valid() and profileform.is_valid()):
            user=userform.save()
            user.set_password(user.password)
            user.save()
            Profile=profileform.save(commit=False)
            Profile.user=user
            if('profile_pic' in req.FILES):
                Profile.profile_pic=req.FILES['profile_pic']
            Profile.save()
            registered=True
            print(register)
        else:
            print("ERROR")
    else:
        userform=UserForm()
        profileform=UserProfile()
    return render(req,"basicapp/register.html",{'registered':registered,'userform':userform,'profileform':profileform})

def login_user(req):
    if(req.method=='POST'):
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(username=username,password=password)
        if(user):
            if(user.is_active):
                login(req,user)
                return HttpResponseRedirect(reverse('basicapp:dashboard'))
            else:
                HttpResponse('Your account is not active')
        else:
            HttpResponse('Invalid account details')
    else:
        return render(req,'basicapp/login.html')
