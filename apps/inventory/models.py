from ckeditor.fields import RichTextField
from django.db import models


class Tag(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Item(models.Model):
    name = models.CharField('Name', max_length=255)
    description = RichTextField('Description', blank=True)
    image = models.ImageField('Image', blank=True, null=True)
    quantity = models.IntegerField('Quantity', default=1)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.quantity})'

    class Meta:
        ordering = ['name']