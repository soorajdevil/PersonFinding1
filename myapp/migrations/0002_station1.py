# Generated by Django 4.2.5 on 2023-10-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station_id', models.IntegerField(null=True)),
                ('Address_line1', models.CharField(max_length=100)),
                ('Address_line2', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Pin', models.IntegerField(null=True)),
                ('Contact_number', models.IntegerField(null=True)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]