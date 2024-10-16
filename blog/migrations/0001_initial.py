# Generated by Django 4.2.16 on 2024-10-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('text', models.TextField()),
                ('published', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
    ]