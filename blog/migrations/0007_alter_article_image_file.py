# Generated by Django 4.2.16 on 2024-12-09 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
