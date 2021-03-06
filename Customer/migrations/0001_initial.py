# Generated by Django 2.2.1 on 2022-06-10 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agent', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('driver', models.CharField(choices=[('Assigned', 'Assigned'), ('Not Assigned', 'Not Assigned')], max_length=200, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Not Recived', 'Not Recived'), ('Delivered', 'Delivered')], default='Not Assigned', max_length=200, null=True)),
                ('castl', models.IntegerField(default=0)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Agent.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Total_Amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('Paid_status', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=200, null=True)),
                ('TransactionCode', models.CharField(max_length=200, null=True)),
                ('MarchentId', models.CharField(max_length=200, null=True)),
                ('Customer_order_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer_order')),
            ],
        ),
    ]
