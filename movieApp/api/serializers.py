from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    genres = GenresSerializer(many=True)
    actors = ActorsSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'country', 'image', 'date', 'genres', 'actors', 'category', 'time', 'rating',
                  'slug', 'video']


class FavMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = FavMovie
        fields = ['id', 'movie', 'user']
