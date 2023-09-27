from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

for ct in ContentType.objects.filter(app_label='logger'):
    admin.site.register(ct.model_class())
