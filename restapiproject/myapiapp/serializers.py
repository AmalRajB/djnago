from rest_framework import serializers
from .models import todolist

class todoserializers(serializers.ModelSerializer):
    class Meta:
        model =todolist
        fields = '__all__'