"""Inventory utils."""
# Django
from django.db.models import Q

CSS_CLASSES = {
    'CharField': {
        'field': 'form-control',
        'label': '',
    },
    'IntegerField': {
        'field': 'form-control',
        'label': '',
    },
    'EmailField': {
        'field': 'form-control',
        'label': '',
    },
    'SlugField': {
        'field': 'form-control',
        'label': '',
    },
    'TypedChoiceField': {
        'field': 'form-control bs-select',
        'label': '',
    },
    'PasswordField': {
        'field': 'form-control',
        'label': '',
    },
    'SetPasswordField': {
        'field': 'form-control',
        'label': '',
    },
    'BooleanField': {
        'field': 'form-check-input',
        'label': '',
    },
    'RegexField': {
        'field': 'form-control',
        'label': '',
    },
    'TreeNodeChoiceField': {
        'field': 'form-control bs-select',
        'label': '',
    },
    'ImageField': {
        'field': '',
        'label': '',
    },
    'FileField': {
        'field': '',
        'label': '',
    },
    'MoneyField': {
        'field': 'form-control',
        'label': '',
    },
    'DecimalField': {
        'field': 'form-control',
        'label': '',
    },
    'DateField': {
        'field': 'form-control custom-datepicker',
        'label': '',
    },
    'DateTimeField': {
        'field': 'form-control custom-datepicker',
        'label': '',
    },
    'DurationField': {
        'field': 'form-control',
        'label': '',
    },
    'SimpleArrayField': {
        'field': 'form-control',
        'label': '',
    },
    'URLField': {
        'field': 'form-control',
        'label': '',
    },
    'NullCharField': {
        'field': 'form-control',
        'label': '',
    },
    'MultipleFileField': {
        'field': '',
        'label': '',
    },
    'FloatField': {
        'field': 'form-control',
        'label': '',
    },
    'PhoneNumberField': {
        'field': 'form-control',
        'label': '',
    },
}


def clean_filter(filter_dict):
    return {key: val for key, val in filter_dict.items() if val and val != ' '}


def filter_to_item_query(filter_dict):
    new_dict = {
        'tags__pk__in': filter_dict.get('tags'),
        'name__istartswith': filter_dict.get('starts_with'),
        'location': filter_dict.get('location'),
        'location__isnull': filter_dict.get('no_location')
    }
    name = filter_dict.get('name')
    q_filter = []
    if name:
        q_filter.append(Q(description__icontains=name) | Q(name__icontains=name))
    new_dict = clean_filter(new_dict)
    return new_dict, q_filter


def set_bootstrap_class(fields):
    """Set Bootstrap classes for specific fields."""
    for _, field in fields.items():
        try:
            field.widget.attrs.update(
                {
                    'class': CSS_CLASSES[field.__class__.__name__]['field'],
                },
            )
        except KeyError:
            pass
