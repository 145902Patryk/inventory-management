def clean_filter(filter_dict):
    return {key: val for key, val in filter_dict.items() if val and val != ' '}


def filter_to_item_query(filter_dict):
    new_dict = {
        'name__icontains': filter_dict.get('name'),
        'tags__pk__in': filter_dict.get('tags'),
        'name__istartswith': filter_dict.get('starts_with'),
    }
    new_dict = clean_filter(new_dict)
    return new_dict
