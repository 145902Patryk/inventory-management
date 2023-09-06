# Django
from django.urls import path

# Local
from .views import ItemsListView
from .views import clear_filters
from .views import set_filters

app_name = 'inventory'


urlpatterns = [
    path('', ItemsListView.as_view(), name='items_list'),
    path('set-filter/', set_filters, name='set_filters'),
    path('clear-filter/', clear_filters, name='clear_filters'),
]