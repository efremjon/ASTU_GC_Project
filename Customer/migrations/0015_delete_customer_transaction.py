# Generated by Django 3.2.9 on 2022-05-23 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0014_customer_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer_Transaction',
        ),
    ]