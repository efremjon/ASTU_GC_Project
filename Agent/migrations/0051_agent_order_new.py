# Generated by Django 3.2.9 on 2022-05-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0050_agent_order_beerr'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent_order',
            name='NEW',
            field=models.IntegerField(default=0),
        ),
    ]