# Generated by Django 3.2.9 on 2022-06-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0087_agent_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='marchentId',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
