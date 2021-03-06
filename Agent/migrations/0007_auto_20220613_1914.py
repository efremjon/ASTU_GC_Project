# Generated by Django 2.2.1 on 2022-06-14 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0006_auto_20220613_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='Adderes',
        ),
        migrations.AddField(
            model_name='driver',
            name='Drive_license',
            field=models.FileField(blank=True, null=True, upload_to='License'),
        ),
        migrations.AddField(
            model_name='driver',
            name='Status',
            field=models.CharField(choices=[('on_duty', 'on_duty'), ('on_garage', 'on_garage'), ('on_wating', 'on_wating')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Profile/'),
        ),
    ]
