from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from Userauth.models import Users
from movies.models import movies, movies_details


class Home(View):
    def get(self, request,api=None):
        if request.user:
            user = request.user
            movies_detail = movies.objects.filter(soft_delete=False).annotate(avg=Avg('movies_info__movie_rating'))
            context = {'movies': movies_detail, 'user': user}
            if request.GET.get('api') == 'angular':
                return JsonResponse({'statusCode': 200,'message': list(movies_detail.values()) })
            return render(request, 'movies.html', context)
        else:
            movies_detail = movies.objects.filter(soft_delete=False).annotate(avg=Avg('movies_info__movie_rating'))
            context = {'movies': movies_detail}
            return render(request, 'movies.html', context)

    def post(self, request):
        User = Users.objects.get(email=request.user)
        if request.POST and request.FILES:
            movies.objects.create(
                movie_name=request.POST['movie_name'],
                movie_genre=request.POST['movie_genre'],
                movie_language=request.POST['movie_language'],
                movie_image=request.FILES['movie_image'],
                user_added=User
            )
            return JsonResponse({'status': 'success', 'message': 'Movie Added'})
        else:
            if request.POST['movie_url'] == '':
                return JsonResponse({'status': 'error'})

            movie_obj = movies()
            movie_obj.get_image_from_url(request.POST['movie_url'], request.POST['movie_name'])
            movie_obj.movie_name = request.POST['movie_name']
            movie_obj.movie_genre = request.POST['movie_genre']
            movie_obj.movie_language = request.POST['movie_language']
            movie_obj.movie_url = request.POST['movie_url']
            movie_obj.user_added = User
            movie_obj.save()
            return JsonResponse({'status': 'success', 'message': 'Movie Added'})


class DeleteMovieDetail(View):
    def post(self, request, id):
        movie_obj = movies.objects.get(id=id)
        movie_obj.soft_delete = True
        movie_obj.save()
        return JsonResponse({'status': 'success', 'message': 'Movie Deleted'})


class EditMovieDetail(View):
    def get(self, request, id):
        movie_obj = list(movies.objects.filter(id=id).values())
        return JsonResponse({'status': 'success', 'message': movie_obj[0]})

    def post(self, request, id):
        if request.POST:
            movie_obj = movies.objects.get(id=id)
            movie_obj.movie_name = request.POST['movie_name']
            movie_obj.movie_genre = request.POST['movie_genre']
            movie_obj.movie_language = request.POST['movie_language']
            movie_obj.save()
            return JsonResponse({'status': 'success', 'message': 'Successfully Movie Updated'})


class DetailsMovieDetail(View):
    def get(self, request, id):
        movie_obj = list(movies.objects.filter(id=id).annotate(avg=Avg('movies_info__movie_rating')).values('movie_name','movie_language','movie_image','movie_genre','avg'))
        context = {'movie': movie_obj[0]}
        return render(request, 'details.html', context)
