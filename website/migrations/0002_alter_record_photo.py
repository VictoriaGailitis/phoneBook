# Generated by Django 4.2.3 on 2023-07-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]