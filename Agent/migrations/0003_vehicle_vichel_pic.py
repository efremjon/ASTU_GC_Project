# Generated by Django 2.2.1 on 2022-06-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0002_auto_20220610_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vichel_pic',
            field=models.ImageField(blank=True, null=True, upload_to='vichel_pic/'),
        ),
    ]