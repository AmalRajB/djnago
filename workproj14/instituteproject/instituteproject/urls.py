
from django.urls import path
from workapp import views

urlpatterns = [
    path('', views.formdatafn,name='form'),

]
