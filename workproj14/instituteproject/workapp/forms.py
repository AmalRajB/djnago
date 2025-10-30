from django import forms
from.models import cirtificate

class cirtificateform(forms.ModelForm):
    class Meta:
        model = cirtificate
        fields = '__all__'
        