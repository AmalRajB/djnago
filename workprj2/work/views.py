from django.shortcuts import render

# Create your views here.
def getform(request):
    if request.GET:
        greet = request.GET.get('UserName')
        return render(request,'getform-data.html',{
            'formData':request.GET,
            'greet': greet
        })
    return render(request,'getform.html' )
def postform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('FavoriteColor')
        return render(request,'postform-data.html',{'formdata':request.POST,'name':name,'color':color
        })
    return render(request,'postform.html')

