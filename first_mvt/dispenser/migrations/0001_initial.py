# Generated by Django 4.1.2 on 2022-10-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispenser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=10)),
                ('machine_type', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('purchase', models.CharField(max_length=10)),
            ],
        ),
    ]
