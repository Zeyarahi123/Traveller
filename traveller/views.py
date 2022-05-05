from django.shortcuts import render,redirect
from .models import Destination
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
# taking static data from the folder itself
"""def index(request):
      dest1 = Destination()
      dest1.name = 'Mumbai'
      dest1.desc = 'City Thats Never Sleeps'
      dest1.price = 650
      dest1.img = 'jaipur1.jpg'
      dest1.offer = True
      
      dest2 = Destination()
      dest2.name = 'Hydrabad'
      dest2.desc = 'Firt Biryani then Sherwani'
      dest2.price = 600
      dest2.img = 'jaipur1.jpg'
      dest2.offer = True

      dest3 = Destination()
      dest3.name = 'Bangluru'
      dest3.desc = 'City of Sky'
      dest3.price = 700
      dest3.img = 'mumbai1.jpg'
      dest3.offer = False

      dests = [dest1, dest2, dest3]

      return render(request, "index.html", {'dests': dests})"""

      #return render(request, "index.html")

def index(request):

      dests = Destination.objects.all()
      return render(request, "index.html", {'dests': dests})


