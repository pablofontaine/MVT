# Generated by Django 4.1.2 on 2022-10-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=40)),
                ('value', models.IntegerField()),
                ('owner', models.CharField(max_length=40)),
            ],
        ),
    ]
