from django.shortcuts import render
from .forms import contactform
from .models import contact

def homefn(request):
    return render(request,'home.html')

def contactfn(request):
    if request.method =='POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            extends = {
                'message':'our team will contact you soon...',
                'form':form
            }
            
            return render(request,'contact.html',extends)
    else:
        form = contactform()    
    return render(request,'contact.html',{'form':form})

def aboutfn(request):
    return render(request,'about.html')
