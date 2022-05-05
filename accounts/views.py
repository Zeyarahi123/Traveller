from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from mysql.connector import connection

# Create your views here.

# User Login
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
             auth.login(request, user)
             return redirect("search") #it will redirect to home page
        else:
            messages.info(request,"Invalid User_Name or Password")
            return redirect('login')

    else:
        return render(request, "login.html")


# User registration
def register(request):
     if request.method == 'POST':
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username = request.POST['username']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          email = request.POST['email']

          #we are checking wheather password1 is same as password2 or nor(password1==password2)

          if password1 == password2:
               if User.objects.filter(username=username).exists():  # it will check wheather same username is available or not in database
                     #print("User_Name is already available") #it will print on terminal
                      messages.info(request,'User_Name is already taken')  #it will give message on same form
                      return redirect('register') #it will send again to register form

               elif User.objects.filter(email=email).exists():  #it will check same email is available in database or not
                     #print("Email is already available")    #it will print on terminal
                     messages.info(request, 'Email is already taken') #it will give message on same form
                     return redirect('register') # it will send again to register form

               else:
                     user=User.objects.create_user(username=username, password=password1, email=email,  first_name=first_name, last_name=last_name)
                     user.save();
                     #print("Created SuccessFully")    #it will print on terminal
                     messages.info(request, 'User Created SuccessFully')   #it will give message on same form
                     return redirect("login")
          else:
               #print("Password Not Matching")   #it will print on terminal
               messages.info(request, 'Password is Not Matching')  #it will give message on same form
               return redirect('register')   # it will send again to register form
     else:

          return render(request, "register.html")


# User logout

def logout(request):
    auth.logout(request)
    return redirect('/')





def search(request):
     return render(request,"search.html")


def inser(request):

            return render(request, "inser.html")