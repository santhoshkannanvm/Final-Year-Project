# Generated by Django 4.0.6 on 2023-06-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='r_isotope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=150)),
                ('result', models.CharField(max_length=150)),
            ],
        ),
    ]
