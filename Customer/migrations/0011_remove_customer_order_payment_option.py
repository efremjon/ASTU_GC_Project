# Generated by Django 3.2.9 on 2022-05-23 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0010_alter_customer_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_order',
            name='Payment_Option',
        ),
    ]