from django.urls import include, path
from rest_framework import routers

from djangorest.views import UserViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies',MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
