from urllib.request import urlopen

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class movies(models.Model):
    user_added = models.ForeignKey('Userauth.Users', on_delete=models.CASCADE, related_name='user_added', null=True)
    movie_name = models.CharField(max_length=200,null=True, blank=True)
    movie_genre = models.CharField(max_length=200,null=True, blank=True)
    movie_language = models.CharField(max_length=200,null=True, blank=True)
    movie_image = models.ImageField(upload_to='media/')
    movie_url = models.URLField(blank=True, null=True)
    soft_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.movie_name

    def get_image_from_url(self, movie_url, movie_name):
        img_tmp = NamedTemporaryFile()
        with urlopen(movie_url) as uo:
            assert uo.status == 200
            img_tmp.write(uo.read())
            img_tmp.flush()
        self.movie_image.save(movie_name, File(img_tmp), save=True)
        self.media_url = movie_url


class movies_details(models.Model):
    movie_info = models.ForeignKey(movies,related_name='movies_info',on_delete=models.CASCADE)
    user_info = models.ForeignKey('Userauth.Users', on_delete=models.CASCADE, related_name='user_info', null=True)
    comments = models.CharField(max_length=255,null=True, blank=True)
    movie_rating = models.IntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0),
                                                                                     MaxValueValidator(5)])