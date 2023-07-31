import string

from django import forms
from django.forms.renderers import get_default_renderer
from django.utils.safestring import mark_safe

from .models import Tag


def alphabet():
    characters = ((a, a) for a in string.ascii_uppercase)
    return characters


class RowCheckboxSelectMultiple(forms.CheckboxSelectMultiple):

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        renderer = get_default_renderer()
        html = renderer.render(self.template_name, context)
        html = html.replace('id="id_tags"', 'class="row" id="id_tags"')
        html = html.replace('<div>', '<div class="col-md-4">')
        return mark_safe(html)


class FilterForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=RowCheckboxSelectMultiple
    )
    starts_with = forms.ChoiceField(
        required=False,
        choices=alphabet(),
        widget=forms.RadioSelect,
    )

    def clean_tags(self):
        return list(self.cleaned_data['tags'].values_list('pk', flat=True))
