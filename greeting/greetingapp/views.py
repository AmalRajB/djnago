from django.shortcuts import render
def greeting(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
