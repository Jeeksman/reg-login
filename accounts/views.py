from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
            
        else:
            messages.info(request,"please Register")
            return redirect('login')
    
    return render (request,'login.html')
    
def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        e_mail=request.POST['e_mail']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Already taken")
                return redirect('register')
            elif User.objects.filter(email=e_mail).exists():
                messages.info(request,"Already exists")
                return redirect('register')
            else:
                user=User.objects.create(username=username,password=password,first_name=firstname,last_name=lastname,email=e_mail)
                user.save()
                print("USER CREATED")
        else:  
            messages.info(request,"password does not match")
            return redirect('register')
            
        return redirect('/')
    else:
         return render(request,'registration.html')