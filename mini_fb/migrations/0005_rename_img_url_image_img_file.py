# Generated by Django 4.2.16 on 2024-10-23 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img_url',
            new_name='img_file',
        ),
    ]
