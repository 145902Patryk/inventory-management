# Django
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.contenttypes.models import ContentType

from .models import Log


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_filter = [
        'content_type',
        'action_flag',
    ]


@admin.register(Log)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'user',
        'status',
    ]
    list_filter = [
        'user',
        'status',
    ]


for ct in ContentType.objects.filter(app_label='logger'):
    try:
        admin.site.register(ct.model_class())
    except AlreadyRegistered:
        pass
