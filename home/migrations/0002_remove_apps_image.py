# Generated by Django 3.1.2 on 2021-01-07 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apps',
            name='image',
        ),
    ]
