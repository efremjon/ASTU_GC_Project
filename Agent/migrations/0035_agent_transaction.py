# Generated by Django 3.2.9 on 2022-05-19 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0034_delete_agent_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Total_Amount', models.FloatField(null=True)),
                ('Paid_status', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=200, null=True)),
                ('delivery_status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('TransactionCode', models.CharField(max_length=200, null=True)),
                ('MarchentId', models.CharField(max_length=200, null=True)),
                ('Agent_order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Agent.agent_order')),
            ],
        ),
    ]
