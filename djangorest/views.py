from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny

from movies.models import movies


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MovieSerializer(serializers.ModelSerializer):
    user_added = UserSerializer(read_only=True)
    movie_name = serializers.CharField(max_length=10,allow_null=False)
    movie_language = serializers.CharField(max_length=10,allow_null=False)
    movie_genre = serializers.CharField(max_length=10,allow_null=False)
    # movie_name = serializers.CharField(max_length=10,allow_null=False)
    class Meta:
        model = movies
        fields = '__all__'
        lookup_field = ['user_added']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    # lookup_field = 'user_added'

