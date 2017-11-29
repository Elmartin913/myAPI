from rest.models import Movie
from rest.serializers import MovieSerializer
from rest_framework import generics


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
