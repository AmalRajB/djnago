from django.urls import path
from crudapp import views

urlpatterns = [
    path('',views.formdatafn,name='home'),
    path('form',views.libraryfn,name='form'),
    path('update/<int:id>/',views.updatefn,name='update'),
    path('delete/<int:id>/',views.deletefn,name='delete'),
]