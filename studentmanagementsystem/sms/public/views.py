from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from . models import Signup
from django .http import HttpResponse
from django.contrib import messages

# Create your views here.
def signup(request):
    return render(request,"sign-up.html")


def courses(request):
   return render(request,"courses.html")

def dashboard(request):
   return render(request,"dashboard.html")

def employees(request):
   return render(request,"employees.html")

def index(request):
   return render(request,"index.html")

def notifications(request):
   return render(request,"notifications.html")

def pg_dashboard(request):
   return render(request,"pg_dashboard.html")

def profile(request):
   return render(request,"profile.html")

def tables(request):
   return render(request,"tables.html")

def tenants(request):
   return render(request,"tenants.html")

def viewstudents(request):
   return render(request,"viewstudents.html")


def signupdata(request):
    if request.method  == 'POST':
      name= request.POST['name']
      email=request.POST['email']
    #   phone=request.POST['phone']
      password=make_password(request.POST['password'])
      if Signup.objects.filter(email=email).exists():
        messages.error(request,"email already exists")
        
    #   elif Register.objects.filter(phone=phone).exists():
    #         messages.error(request,"contact already exists")
      else:
            Signup.objects.create(name=name,email=email,password=password) 
            return render(request,'index.html')

    else:
         return render(request,'sign-up.html')

def logindata(request):
      if request.method == 'POST':
         email = request.POST['email']
         password = request.POST['password']
         if Signup.objects.filter(email=email).exists():
          obj= Signup.objects.get(email=email)
          Password=obj.password
          if check_password(password,Password):
                return render(request,"dashboard.html")
          else:
                return HttpResponse("password did not match")
         else:
                return HttpResponse("email did not match")



       

  
