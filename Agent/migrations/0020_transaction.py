# Generated by Django 3.2.9 on 2022-05-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0019_remove_agent_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Total_Amount', models.FloatField(null=True)),
                ('Paid_status', models.CharField(choices=[('Payed', 'Pending'), ('Not Payed', 'Out for delivery')], max_length=200, null=True)),
                ('delivery_status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('TransactionCode', models.CharField(max_length=200, null=True)),
                ('MarchentId', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
