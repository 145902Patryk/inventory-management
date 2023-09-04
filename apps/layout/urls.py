from django.urls import path

from .views import MainLayoutView

app_name = 'layout'


urlpatterns = [
    path('', MainLayoutView.as_view(), name='main'),
]