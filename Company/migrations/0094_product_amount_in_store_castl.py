# Generated by Django 3.2.9 on 2022-06-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0093_auto_20220608_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_amount_in_store',
            name='castl',
            field=models.IntegerField(default=0),
        ),
    ]
