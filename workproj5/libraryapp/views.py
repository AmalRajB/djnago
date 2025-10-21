from django.shortcuts import render
from .forms import libraryform,customersform
from .models import library,customers

def libraryfn(request):
    if request.method =='POST':
        form = libraryform(request.POST)
        if form.is_valid():
            db = form.save()
            return render(request,'message.html')
    else:
        form = libraryform()
    return render(request,'libraryform.html',{'form':form})    

def librarydatafn(request):
    data = library.objects.all()
    return render(request,'librarydata.html',{'data':data})   

def customerfn(request):
    if request.method =='POST':
        form = customersform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'message.html')
    else:
        form = customersform()
    return render(request,'customerform.html',{'form':form}) 

def customerdata1(request):
    data = customers.objects.order_by('name') 
    return render(request,'customerfulldata.html',{'data':data})

def customerdata2(request):
    data = customers.objects.filter(email__contains='@example.com')
    return render(request,'customerdata2.html',{'data':data})


