# Generated by Django 4.2.5 on 2024-01-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_hospitals_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='proof',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
