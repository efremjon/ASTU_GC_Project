# Generated by Django 3.2.9 on 2022-05-21 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0083_product_amount_in_store_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_to_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=200, null=True)),
                ('qunitiy', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Store', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company_store')),
            ],
        ),
    ]
