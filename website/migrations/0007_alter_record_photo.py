# Generated by Django 4.2.3 on 2023-07-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_record_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='photo',
            field=models.ImageField(upload_to='website/files/'),
        ),
    ]
