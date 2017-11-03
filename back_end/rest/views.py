from django.shortcuts import render
from .models import Person, Movie
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response, Serializer

# Create your views here.

class MoviesListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()