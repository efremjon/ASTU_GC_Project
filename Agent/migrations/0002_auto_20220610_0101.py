# Generated by Django 2.2.1 on 2022-06-10 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent_transaction',
            name='scheduled_for',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agent_transaction',
            name='scheduled_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]