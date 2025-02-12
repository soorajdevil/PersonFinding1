# Generated by Django 4.2.5 on 2023-12-11 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_casesheet_age_alter_casesheet_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enquiry_detail', models.CharField(max_length=100)),
                ('Date', models.DateField(max_length=100)),
                ('hospital_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.hospitals')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.users')),
            ],
        ),
    ]
