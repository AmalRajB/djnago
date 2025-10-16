from django.shortcuts import render
from .forms import myform
def greeting(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def formfn(request):
    if request.method == 'POST':
        form = myform(request.POST)
        return render(request,'formdata.html',{'form':form})
    else:
        form = myform()
        return render(request,'form.html',{'form':form})

