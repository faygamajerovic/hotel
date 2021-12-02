from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.



def homepage(request):


    return render(request,'pages/homepage.html')



def contact(request):


    return render(request,'pages/contact.html')