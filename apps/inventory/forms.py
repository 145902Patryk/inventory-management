from django import forms

from .models import Tag


class FilterForm(forms.Form):
    DEMO_CHOICES = (
        ("1", "Naveen"),
        ("2", "Pranav"),
        ("3", "Isha"),
        ("4", "Saloni"),
    )

    name = forms.CharField(required=False)
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
    )

    def clean_tags(self):
        return list(self.cleaned_data['tags'].values_list('pk', flat=True))
