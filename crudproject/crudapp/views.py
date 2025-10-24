from django.shortcuts import render,redirect
from .forms import libraryform
from .models import library 
from django.core.paginator import Paginator

def libraryfn(request):
    if request.method =='POST':
        form = libraryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = libraryform()
    return render(request,'form.html',{'form':form})             


def formdatafn(request):
    booklist = library.objects.all()
    paginator = Paginator(booklist, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'formdata.html',{'page_obj':page_obj})

def updatefn(request,id):
    data = library.objects.get(pk=id)
    if request.method =='POST':
        form = libraryform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = libraryform(instance=data)
    return render(request,'update.html',{'form':form})    
    
def deletefn(request,id):
    data = library.objects.get(pk=id)
    if request.method =='POST':
        data.delete()
        return redirect('home')
    return render(request,'delete.html',{'data':data})


