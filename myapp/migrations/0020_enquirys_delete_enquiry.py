# Generated by Django 4.2.5 on 2023-12-14 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquirys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enquiry_detail', models.CharField(max_length=100)),
                ('Current_Date', models.DateField()),
                ('hospital_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.hospitals')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.users')),
            ],
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
    ]