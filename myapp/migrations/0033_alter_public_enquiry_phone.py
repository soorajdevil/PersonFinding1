# Generated by Django 4.2.2 on 2023-12-29 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_public_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_enquiry',
            name='Phone',
            field=models.IntegerField(null=True),
        ),
    ]