from django.shortcuts import render
from .forms import loginform,regform
def formfn(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            return render(request,'result.html',{'email':form['email'].value})
    else:
        form = loginform()
    return render(request,'form.html',{'form':form})
    
def regformfn(request):
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            return render(request,'result2.html',{'name':form['name'].value})
    else:
        form = regform()
    return render(request,'form2.html',{'form':form})     


