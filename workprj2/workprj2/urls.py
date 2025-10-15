
from django.urls import path
from work import views

urlpatterns = [
    path('',views.getform ),
    path('form',views.postform)
]
