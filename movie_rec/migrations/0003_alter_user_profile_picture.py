# Generated by Django 4.2.16 on 2024-12-09 03:23

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rec', '0002_movie_list_review_user_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_avatar.jpeg', upload_to=''),
        ),

        # migrations.AlterField(
        #     model_name='recommendation',
        #     name='recom_from',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='movie_rec.user'),
        # ),
        # migrations.AlterField(
        #     model_name='recommendation',
        #     name='recom_for',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='movie_rec.user'),
        # ),
        # migrations.AlterField(
        #     model_name='movie_list',
        #     name='owner',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_holder', to='movie_rec.user'),
        # ),
    ]
