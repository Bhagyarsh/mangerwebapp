# Generated by Django 3.1.4 on 2020-12-15 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
