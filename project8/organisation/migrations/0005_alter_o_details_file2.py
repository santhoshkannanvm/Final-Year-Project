# Generated by Django 4.0.7 on 2023-01-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0004_o_details_file2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='o_details',
            name='file2',
            field=models.FileField(default='exit', upload_to='documents/'),
            preserve_default=False,
        ),
    ]
