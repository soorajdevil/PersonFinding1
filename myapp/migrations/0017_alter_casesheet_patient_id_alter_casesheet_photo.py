# Generated by Django 4.2.5 on 2023-12-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_casesheet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casesheet',
            name='Patient_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='casesheet',
            name='Photo',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
