# Generated by Django 3.2.9 on 2022-06-04 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0054_auto_20220522_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent_order',
            name='NEW',
        ),
        migrations.RemoveField(
            model_name='agent_order',
            name='beerr',
        ),
    ]
