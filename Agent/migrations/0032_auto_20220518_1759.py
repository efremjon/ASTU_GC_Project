# Generated by Django 3.2.9 on 2022-05-19 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0031_agent_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent_transaction',
            name='Agent_order_id',
        ),
        migrations.DeleteModel(
            name='Agent_order',
        ),
    ]
