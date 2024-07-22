from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import table
from django.contrib import messages

# Create your views here.
def home1(request):
    return render (request,'index.html')
def about1(request):
    return render (request,'about.html')
def book(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        date=request.POST.get('date')
        person=request.POST.get('person')
         
        
        if name !='' or email !='' or number !='' or date !='' or person !='':
            data=table(name=name,Email=email,Person=person,Date=date,Number=number)
            data.save()
            return redirect('/')   
    return render (request,'book.html')

def menu(request):
    return render (request,'menu.html')