# Generated by Django 4.0 on 2021-12-21 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_property_title_alter_property_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenities',
            name='gym',
        ),
    ]