# Generated by Django 3.2.8 on 2021-11-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='likesCount',
            field=models.IntegerField(default=0),
        ),
    ]
