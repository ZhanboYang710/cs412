# Generated by Django 4.2.16 on 2024-12-09 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_file',
            field=models.ImageField(blank=True, default='default_avatar.jpeg', upload_to=''),
        ),
    ]
