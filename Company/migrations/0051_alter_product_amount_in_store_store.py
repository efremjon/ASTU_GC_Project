# Generated by Django 3.2.9 on 2022-05-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0050_auto_20220512_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_amount_in_store',
            name='Store',
            field=models.ManyToManyField(to='Company.Company_Store'),
        ),
    ]
