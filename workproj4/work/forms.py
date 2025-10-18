from django import forms
class movieform(forms.Form):
    name = forms.CharField(max_length=100)
    year = forms.IntegerField()
class contactform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput,max_length=100)
    phone = forms.IntegerField()
