from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.contenttypes.models import ContentType

for ct in ContentType.objects.filter(app_label='logger'):
    try:
        admin.site.register(ct.model_class())
    except AlreadyRegistered:
        pass