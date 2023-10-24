# Django
from django.urls import path

# Local
from .views import MainLayoutView, LocationSetItems
from .views import add_location
from .views import items_list_for_location

app_name = 'layout'


urlpatterns = [
    path('', MainLayoutView.as_view(), name='main'),
    path('add-location/', add_location, name='add_location'),
    path('items/', items_list_for_location, name='get_items'),
    path('set-item/<pk>/', LocationSetItems.as_view(), name='set_item'),
]
