from django.urls import path
from apiapp import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('product/',views.product,name='product'),
]

