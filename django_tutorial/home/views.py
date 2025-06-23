from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
# Create your views here
from home.forms import BookingForm



def index(request):
    
    return render(request, 'home/index.html')

def about(request):
    return render(request, "about.html")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return render(request, 'confirmation.html', {'booking': booking})
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def doctors(request):
    dict_docs ={
        'doctors': Doctors.objects.all()
    }

    return render(request, "doctors.html",dict_docs)

def contact(request):
    return render(request, "contact.html")

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, "department.html",dict_dept)




