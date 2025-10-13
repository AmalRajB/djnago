from django.urls import path
from galleryapp import views
urlpatterns = [
  path('home', views.homepage,name='home'),
  path('contact',views.contact,name='contact'),

]
