# Django
from django.urls import path

# Local
from .views import MainLayoutView
from .views import add_location

app_name = 'layout'


urlpatterns = [
    path('', MainLayoutView.as_view(), name='main'),
    path('add-location/', add_location, name='add_location')
]