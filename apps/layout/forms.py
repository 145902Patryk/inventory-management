# Django
from django import forms
from django_select2.forms import Select2MultipleWidget

from apps.inventory.models import Item
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


class SetItemForm(forms.Form):
    items = forms.ModelMultipleChoiceField(
        label='Select items for location',
        queryset=Item.objects.filter(location=None),
        widget=Select2MultipleWidget(),
    )
