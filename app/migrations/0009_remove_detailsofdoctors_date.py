# Generated by Django 3.0.7 on 2020-06-20 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_detailsofdoctors_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailsofdoctors',
            name='date',
        ),
    ]
