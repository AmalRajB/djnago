from django.urls import path
from myapiapp import views 

urlpatterns = [
    path('signup/',views.signupfn,name='signup'),
    path('login/',views.loginfn,name='login'),
    path('todocreate/',views.todocreate,name='todocreate'),
    path('todoview/',views.todoview,name='todoview'),
    path('<int:id>/todoupdate/',views.todoupdate,name='todoupdate'),
    path('<int:id>/tododelete/',views.tododelete,name='tododelete'),



]