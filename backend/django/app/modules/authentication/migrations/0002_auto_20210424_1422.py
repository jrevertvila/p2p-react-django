# Generated by Django 3.0.2 on 2021-04-24 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
