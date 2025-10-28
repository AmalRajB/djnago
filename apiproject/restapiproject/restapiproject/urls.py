
from django.urls import path,include

urlpatterns = [
    path('apiapp/', include('apiapp.urls')),
]
