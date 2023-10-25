# Generated by Django 4.2.3 on 2023-09-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('path', models.CharField(max_length=255)),
                ('response', models.JSONField(blank=True)),
            ],
        ),
    ]
