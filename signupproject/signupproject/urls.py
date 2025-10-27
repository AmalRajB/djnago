
from django.urls import path
from workapp import views

urlpatterns = [
    path('signup',views.signupfn,name='signup'),
    path('login',views.loginfn,name='login'),
    path('',views.welcomefn,name='home'),
    path('logout',views.logoutfn,name='logout'),

]
