from django.db.models import Q


def clean_filter(filter_dict):
    return {key: val for key, val in filter_dict.items() if val and val != ' '}


def filter_to_item_query(filter_dict):
    new_dict = {
        'tags__pk__in': filter_dict.get('tags'),
        'name__istartswith': filter_dict.get('starts_with'),
        'location': filter_dict.get('location')
    }
    name = filter_dict.get('name')
    q_filter = []
    if name:
        q_filter.append(Q(description__icontains=name) | Q(name__icontains=name))
    new_dict = clean_filter(new_dict)
    return new_dict, q_filter
