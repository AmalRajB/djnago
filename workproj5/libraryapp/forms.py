from django import forms
from .models import library,customers

class libraryform(forms.ModelForm):
    class Meta:
        model = library
        fields = '__all__'
class customersform(forms.ModelForm):
    class Meta:
        model = customers
        fields = '__all__'       