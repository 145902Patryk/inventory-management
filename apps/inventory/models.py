"""Inventory models."""
# Django
from django.db import models

# 3rd-party
from ckeditor.fields import RichTextField

# Project
from apps.layout.models import Location


class VisibleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Tag(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:  # noqa: D106
        ordering = ['name']


class Item(models.Model):
    name = models.CharField('Name', max_length=255)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        verbose_name='Location',
        blank=True,
        null=True,
    )
    image = models.ImageField('Image', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    description = RichTextField('Description', blank=True)
    quantity = models.IntegerField('Quantity', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    objects = VisibleManager()
    all_objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:  # noqa: D106
        ordering = ['name']
