# Generated by Django 4.2.5 on 2024-01-27 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_missing_found'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing_found',
            name='found_Usermissing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.usermissingadds'),
        ),
    ]
