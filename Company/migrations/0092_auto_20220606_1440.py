# Generated by Django 3.2.9 on 2022-06-06 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0091_rename_telegram_finance_manager_telegram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_store_manager',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='finance_manager',
            old_name='Address',
            new_name='address',
        ),
    ]