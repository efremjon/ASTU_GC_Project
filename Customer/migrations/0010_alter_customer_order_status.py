# Generated by Django 3.2.9 on 2022-05-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0009_customer_order_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reject', 'Reject'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
