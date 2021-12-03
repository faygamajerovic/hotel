from django.http.response import HttpResponse
from django.shortcuts import render
from staff.models import Hotel
# Create your views here.



def homepage(request):


    return render(request,'pages/homepage.html')



def contact(request):


    return render(request,'pages/contact.html')


def list_hotels(request):

    query = Hotel.objects.all()


    context = {
        "hotels" : query
    }


    return render(request,'pages/list_hotels.html', context=context)