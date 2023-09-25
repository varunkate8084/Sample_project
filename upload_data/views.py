from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *

def UploadFiles(request):
    try:
        if request.method == 'POST':
            data = request.POST
            file_image = request.FILES.get('file_image')
            file_description = data.get('file_description')
            Files.objects.create(
                file_description=file_description,
                file_image=file_image,
                )
            return redirect("/uploaddata")
        queryset = Files.objects.all()
        context = {'files':queryset}
        return render(request,'uploadfiles.html',context)
    except Exception as e:
        print("Errorrrrrr:",e)

def delete_files(request,id):
    try:
        queryset = Files.objects.get(id = id)
        queryset.delete()
        return redirect('/uploaddata/')
    except Exception as e:
        print("Errorrrrrr:",e)

def LogIn_page(request):
    try:
        if request.method =="POST":
            username =request.POST.get('username')
            password =request.POST.get('password')

            if not User.objects.filter(username = username).exists():
                messages.error(request,'Invalid Username')
                return redirect("/login/")
            user = authenticate(username = username, password = password)
            if user is None:
                messages.error(request,"Invalid Password")
                return redirect("/login/")
            else:
                print("inside else")
                login(request,user)
                return redirect("/uploaddata/")
        return render(request,"login.html")
    except Exception as e:
        print("Eroorrrrr:",e)

def Registration(request):
    try:
        if request.method =="POST":
            first_name=request.POST.get('first_name')
            last_name =request.POST.get('last_name')
            username =request.POST.get('username')
            email =request.POST.get('email')
            password =request.POST.get('password')

            user = User.objects.filter(username= username)
            if user.exists():
                messages.info(request, "Username Already Taken..")
                return redirect('/registration')

            user = User.objects.create(
                first_name =first_name,
                last_name = last_name,
                username = username ,
                email = email,
            )
            user.set_password(password)
            user.save()
            messages.info(request, "User Successfully Registered..")

            return redirect('/registration/')
        return render(request,"registration.html")
    except Exception as e:
        print("errorrrrrrrrrrrrrrrrr*******",e)

def logout_page(request):
    logout(request)
    return redirect('/login/')

