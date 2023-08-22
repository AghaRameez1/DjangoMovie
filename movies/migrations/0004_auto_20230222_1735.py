# Generated by Django 3.2.12 on 2023-02-22 12:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userauth', '0001_initial'),
        ('movies', '0003_moviesdetails_soft_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(blank=True, max_length=200, null=True)),
                ('movie_genre', models.CharField(blank=True, max_length=200, null=True)),
                ('movie_language', models.CharField(blank=True, max_length=200, null=True)),
                ('movie_image', models.ImageField(upload_to='media/')),
                ('movie_url', models.URLField(blank=True, null=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_added', to='Userauth.users')),
            ],
        ),
        migrations.CreateModel(
            name='movies_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_rating', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('movie_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.movies')),
                ('user_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to='Userauth.users')),
            ],
        ),
        migrations.DeleteModel(
            name='moviesdetails',
        ),
    ]
