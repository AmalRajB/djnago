
from django.urls import path
from workapp import views

urlpatterns = [
    path('', views.employeefn),
    path('student', views.studentfn),

]
