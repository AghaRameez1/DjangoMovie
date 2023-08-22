from django.contrib import admin

# Register your models here.
from movies.models import movies, movies_details


class MovieAdmin(admin.ModelAdmin):
    list_display = ('user_added','movie_name', 'movie_genre', 'movie_language','movie_image','movie_url','soft_delete')

admin.site.register(movies, MovieAdmin)

class MovieDetailsAdmin(admin.ModelAdmin):
    list_display = ('user_info','movie_info', 'comments','movie_rating')


admin.site.register(movies_details, MovieDetailsAdmin)