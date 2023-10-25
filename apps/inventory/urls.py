"""Inventory urls."""
# Django
from django.urls import path

# Local
from .views import ItemCreateView
from .views import ItemDeleteView
from .views import ItemsListView
from .views import ItemUpdateView
from .views import clear_filters
from .views import remove_item
from .views import set_filters

app_name = 'inventory'


urlpatterns = [
    path('', ItemsListView.as_view(), name='items_list'),
    path('set-filter/', set_filters, name='set_filters'),
    path('clear-filter/', clear_filters, name='clear_filters'),
    path('add-item/<int:location_pk>/', ItemCreateView.as_view(), name='add_item_location'),
    path('add-item/', ItemCreateView.as_view(), name='add_item'),
    path('edit-item/<pk>/', ItemUpdateView.as_view(), name='edit_item'),
    path('delete-item/<pk>/', ItemDeleteView.as_view(), name='delete_item'),
    path('remove-item/', remove_item, name='remove_item'),
]
