# Generated by Django 3.2.9 on 2022-05-21 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0084_add_to_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_to_store',
            name='Store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company_store'),
        ),
    ]