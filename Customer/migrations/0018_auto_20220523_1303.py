# Generated by Django 3.2.9 on 2022-05-23 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0017_remove_customer_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_transaction',
            name='Customer_order_id',
        ),
        migrations.DeleteModel(
            name='Customer_order',
        ),
    ]
