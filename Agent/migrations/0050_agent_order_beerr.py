# Generated by Django 3.2.9 on 2022-05-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0049_alter_agent_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent_order',
            name='beerr',
            field=models.IntegerField(default=0),
        ),
    ]
