from rest.models import Movie
from rest.serializers import MovieSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(APIView):
    def get_object(self, id):
        id = int(id)
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        id = int(id)
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id, format=None):
        id = int(id)
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serialier.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        id = int(id)
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
