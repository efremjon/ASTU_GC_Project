# Generated by Django 3.2.9 on 2022-05-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0082_product_amount_in_store_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_amount_in_store',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
