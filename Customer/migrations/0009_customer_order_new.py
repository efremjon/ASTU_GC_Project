# Generated by Django 3.2.9 on 2022-05-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_customer_order_beerr'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_order',
            name='NEW',
            field=models.IntegerField(default=0),
        ),
    ]
