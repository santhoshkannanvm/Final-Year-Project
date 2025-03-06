# Generated by Django 4.0.7 on 2023-01-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='process_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
