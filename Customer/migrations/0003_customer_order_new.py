# Generated by Django 2.2.1 on 2022-06-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_remove_customer_order_castl'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_order',
            name='new',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]