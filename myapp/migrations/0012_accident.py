# Generated by Django 4.2.5 on 2023-12-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_usermissingadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Contact_Number', models.CharField(max_length=100)),
                ('Accident_Details', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
    ]
