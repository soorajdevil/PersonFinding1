# Generated by Django 4.2.5 on 2023-12-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_accident1_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident1',
            name='Video',
            field=models.FileField(default='timezone.now()', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]