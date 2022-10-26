from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class MovieAPIList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieAPIGet(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_object(self):
        item = self.kwargs.get('slug')
        return Movie.objects.get(slug=item)


class FavMovies(generics.ListCreateAPIView):
    queryset = FavMovie.objects.all()
    serializer_class = FavMovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return FavMovie.objects.filter(user=user)
