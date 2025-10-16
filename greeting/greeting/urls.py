
from django.urls import path
from greetingapp import views
urlpatterns = [
   
    path('home',views.greeting),
    path('about',views.about),
    path('form',views.formfn),

]
