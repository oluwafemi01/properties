from django import forms
from django.contrib.auth.models import User
from .models import properties

class propertiesForm(forms.ModelForm):
    class Meta:
        model = properties
        fields = [
        		'title',
                'description',
                'location',
                'image',
                'bathroom',
                'room'
            ]
        

