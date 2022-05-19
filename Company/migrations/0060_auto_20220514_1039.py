# Generated by Django 3.2.9 on 2022-05-14 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0059_remove_product_amount_in_store_product_quintitiy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_amount_in_store',
            name='store',
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company_store'),
        ),
    ]
