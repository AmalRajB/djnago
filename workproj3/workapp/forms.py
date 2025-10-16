from django import forms
from django.core.validators import validate_email
from django.core.validators import ValidationError

def validate_not_gmail(value):
    if value.find('@gmail') != -1:
        raise ValidationError(
            "Gmail is not allowed",
            params={'value': value},
        )

class loginform(forms.Form):
    email = forms.CharField(validators=[validate_email,validate_not_gmail])
    password = forms.CharField(min_length=6,max_length=8)

class regform(forms.Form):
    name = forms.CharField(max_length=50,min_length=5)
    email = forms.EmailField()
    password = forms.CharField(max_length=20,min_length=8) 
       
