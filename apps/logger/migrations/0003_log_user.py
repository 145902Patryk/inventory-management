# Generated by Django 4.2.3 on 2023-10-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_rename_start_log_created_remove_log_end_log_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
