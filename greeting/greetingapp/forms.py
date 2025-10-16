from django import forms
class myform(forms.Form):
    email = forms.CharField()
    password = forms.CharField()