

from django.urls import path
from workapp import views

urlpatterns = [
    path('',views.formfn),
    path('form2',views.regformfn)
]
