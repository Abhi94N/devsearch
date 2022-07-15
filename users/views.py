from django.shortcuts import render, redirect
from .models import Profile

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.

def loginUser(request):
    page = 'login'

    
    # if user is authenticated
    if request.user.is_authenticated:
        redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
        
        # queries database and finds user in Users table and login
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # login function creates a session table in the database and gets session ID in browsers cookies(how app knows user logs in)
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'Username OR password is incorrect')
    context = {'page': page}
    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    context = {}
    # deletes session
    logout(request)
    messages.success(request,'Username was logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        #passes in body of post to create user
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #doesn't save right away
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
            
            #login user
            login(request, user)
            return redirect('profiles')
        else:
           messages.error(request, 'An error has occurred during registration')             
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    #exclude skipps with out description
    topSkills = profile.skill_set.exclude(description__exact="") 
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html',context)