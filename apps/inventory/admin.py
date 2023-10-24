# Django
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.contenttypes.models import ContentType

# Local
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'location', 'created_at']


for ct in ContentType.objects.filter(app_label='inventory'):
    try:
        admin.site.register(ct.model_class())
    except AlreadyRegistered:
        pass
