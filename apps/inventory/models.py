from ckeditor.fields import RichTextField
from django.db import models

from apps.layout.models import Location


class Tag(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
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

    def __str__(self):
        return f'{self.name} ({self.quantity})'

    class Meta:
        ordering = ['name']