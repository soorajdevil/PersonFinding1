# Generated by Django 4.2.5 on 2023-11-18 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_hospitals_delete_hospital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user_type',
            new_name='usertype',
        ),
    ]
