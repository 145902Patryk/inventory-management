"""Inventory forms."""

# Standard Library
import string

# Django
from django import forms
from django.forms.renderers import get_default_renderer
from django.utils.safestring import mark_safe

# 3rd-party
from django_select2.forms import Select2MultipleWidget
from django_select2.forms import Select2Widget

# Project
from apps.layout.models import Location

# Local
from .models import Item
from .models import Tag
from .utils import set_bootstrap_class


def alphabet():
    characters = ((a, a) for a in string.ascii_uppercase)
    return characters


class TagsWidget(Select2MultipleWidget):
    search_fields = [
        'name__icontains',
    ]


class RowCheckboxSelectMultiple(forms.CheckboxSelectMultiple):

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        renderer = get_default_renderer()
        html = renderer.render(self.template_name, context)
        html = html.replace('id="id_tags"', 'class="row" id="id_tags"')
        html = html.replace('<div>', '<div class="col-md-4">')
        return mark_safe(html)


class FilterForm(forms.Form):
    name = forms.CharField(
        label='Name/Description',
        required=False,
    )
    location = forms.ModelChoiceField(
        label='Location',
        required=False,
        queryset=Location.objects.all().exclude(layout=None).order_by('layout__name', 'name'),
        widget=Select2Widget,
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=RowCheckboxSelectMultiple,
    )
    no_location = forms.BooleanField(
        label='Show items without location set',
        required=False,
    )
    starts_with = forms.ChoiceField(
        required=False,
        choices=alphabet(),
        widget=forms.RadioSelect,
    )

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes to all fields."""
        super().__init__(*args, **kwargs)
        set_bootstrap_class(self.fields)

    def clean_tags(self):
        return list(self.cleaned_data['tags'].values_list('pk', flat=True))

    def clean_location(self):
        loc = self.cleaned_data['location']
        if loc:
            return loc.pk


class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes to all fields."""
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        pk = initial.get('location_pk')
        if isinstance(pk, int):
            self.fields['location'].initial = pk
            self.fields['location'].disabled = True
        set_bootstrap_class(self.fields)

    class Meta:  # noqa: D106
        model = Item
        fields = '__all__'
        exclude = ['deleted']
        widgets = {
            'location': Select2Widget,
            'tags': TagsWidget,
        }
