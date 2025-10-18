from django.shortcuts import render
from .forms import movieform,contactform
from .models import movie,contact

# Create your views here.
def movieformfn(request):
    if request.method == 'POST':
        form = movieform(request.POST)
        if form.is_valid():
            cust = movie()
            cust.name = form.cleaned_data['name']
            cust.year = form.cleaned_data['year']
            cust.save()
            return render(request,'result.html',{
                 'name':form['name'].value,
                 'year':form['year'].value
            })
    else:
        form = movieform()
    return render(request,'movieform.html',{'form':form})

def contactformfn(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            db = contact()
            db.name = form.cleaned_data['name']
            db.email = form.cleaned_data['email']
            db.phone = form.cleaned_data['phone']
            db.save()
            name = form['name'].value
            return render(request,'result2.html',{'name':name})
    else:
        form = contactform()
    return render(request,'contactform.html',{'form':form})        

