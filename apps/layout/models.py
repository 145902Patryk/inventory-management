"""Layout models."""
# Django
from django.db import models


class Layout(models.Model):
    name = models.CharField('Name', max_length=255)
    image = models.ImageField('Image', blank=True, null=True)
    order = models.IntegerField('Order', default=100)

    def __str__(self):
        return self.name

    class Meta:  # noqa: D106
        ordering = ['order']


class Location(models.Model):
    name = models.CharField('Name', max_length=255)
    layout = models.ForeignKey(
        Layout,
        on_delete=models.SET_NULL,
        verbose_name='Layout',
        blank=True,
        null=True,
    )
    x = models.FloatField('Left')
    y = models.FloatField('Top')

    def __str__(self):
        if self.layout:
            return f'{self.layout.name} - {self.name}'
        return f'None - {self.name}'

    class Meta:  # noqa: D106
        ordering = ['layout', 'name']
