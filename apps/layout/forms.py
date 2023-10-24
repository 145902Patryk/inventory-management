"""Layout forms."""
# Django
from django import forms

# 3rd-party
from django_select2.forms import Select2MultipleWidget

# Project
from apps.inventory.models import Item
from apps.layout.models import Location


class LocationForm(forms.ModelForm):
    class Meta:  # noqa: D106
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
