from django.shortcuts import render ,HttpResponse ,redirect 
from home.models import Contact
from django.http import JsonResponse
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
import smtplib

# Create your views here.


def index(request):
    return render(request , "home/index.html")
    
# contact page 

def contact(request):
    if request.method == "POST":
       name = request.POST["name"]
       email = request.POST["email"]
       massage = request.POST["massage"]
       
       if len(name)<4 or len(email)<6 or len(massage)<10:
           
           messages.error(request, 'form fill correctly ')
       else:
           
           s = smtplib.SMTP('smtp.gmail.com', 587)
           s.starttls()
           s.login("surajp9999999@gmail.com", "88406439wp")
           msg = massage
           s.sendmail(email, "surajp9999999@gmail.com", msg)
           s.quit()

           # contact = Contact(name=name,email=email,massege=massage)
           # contact.save()
           messages.success(request,"Form has been submit")
    return render(request,"home/contact.html")

# about page function start here

def about(request):
    return render(request,"home/about.html")
    
    
# sign up function start here 


    
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username,email,password)
        messages.success(request,"Your Account have been created ")
        user.save()
        return redirect("/")
    else:
        pass
        
    return render(request,"home/signup.html")
    
    
    
# log in function start here 


def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username,password)
        user = authenticate(username= username , password= password)
        if user is not None:
              login(request,user)
              messages.success(request,"Your Logged in")
              return redirect("/")
              
              
        else:
            
            messages.error(request, "User Not found")
    return render(request,"home/signin.html")

# log out function start here 

def Logout(request):
    
    logout(request)
    return redirect("/Login")
def api(request):
    data = {
        'name':'suraj',
        'age':21,
        'adrass':'hom',
    }
    return JsonResponse(data)
