# Generated by Django 3.2.9 on 2022-05-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0053_auto_20220521_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='Telegram',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='about',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='instagrm',
        ),
        migrations.AddField(
            model_name='customer',
            name='House_No',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vichel_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vichel_type',
            field=models.CharField(choices=[('Fetch track:', 'Fetch track'), ('Distribution track', 'Distribution track')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Agent_Store_Manager',
        ),
    ]