from django import forms

from apps.layout.models import Location


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'