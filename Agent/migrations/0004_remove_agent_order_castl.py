# Generated by Django 2.2.1 on 2022-06-13 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0003_vehicle_vichel_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent_order',
            name='castl',
        ),
    ]
