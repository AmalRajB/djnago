from django import forms
from .models import library

class libraryform(forms.ModelForm):
    class Meta:
        model = library
        fields = ['book_name','author','year']


        widgets = {
            'book_name': forms.TextInput(attrs={
                'placeholder': 'BookName'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'AuthorName'
            }),
            'year': forms.TextInput(attrs={
                'placeholder': 'Year'
            })
        }