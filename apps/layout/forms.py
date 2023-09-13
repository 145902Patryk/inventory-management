# Django
from django import forms

# Project
from apps.layout.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'layout': forms.HiddenInput(),
            'x': forms.HiddenInput(),
            'y': forms.HiddenInput(),
        }
