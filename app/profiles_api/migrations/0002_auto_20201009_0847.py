# Generated by Django 2.1.15 on 2020-10-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]