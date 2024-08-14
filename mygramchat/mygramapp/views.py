from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import*

# Create your views here.
def index(request):
    feeds= Feedpost.objects.all().order_by('-id')
    if 'username' not in request.session:
        return redirect("usersignin")
    return render(request,"index.html",{"feeds":feeds})
def usersignin(request):
    if 'username' in request.session:
        return redirect('index', user=request.user.username)  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('index')  
        
    return render(request,"signin.html")
def usersignup(request):
    if request.POST:
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if not username or not email or not password or not confirmpassword:
            messages.error(request,'all fields are required.')

        elif confirmpassword != password:
            messages.error(request,"password doesnot match")
           
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exist")
           
        elif User.objects.filter(username=username).exists():
            messages.error(request,"username already exist")

        else:
           
            user = User.objects.create_user(username=username, email=email, password=password)    
            user.save()
            messages.success(request,"account created successfully")
            return redirect("usersignin")
    return render(request,"createuser.html") 

def myfeed(request):
    user = request.user
    feeds = Feedpost.objects.filter(User=user).order_by('-id')
    return render(request,"myfeed.html",{"feeds":feeds})


def newpost(request):
    if request.POST:
        feedimage= request.FILES.get("feedimage")  
        description= request.POST.get("description")
        user = request.user
        probj = Feedpost(feedimage=feedimage, description=description,User=user)
        probj.save()
        return redirect("index")
    return render(request,"newpost.html")