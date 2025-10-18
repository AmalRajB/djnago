
from django.urls import path
from work import views

urlpatterns = [
    path('', views.movieformfn),
    path('contact',views.contactformfn),
]
