from rest_framework import serializers
from .models import Person, Movie


class PersonSerializator(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'surname')


class MovieSerializator(serializers.ModelSerializer):
    actor = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    director = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.all())
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', )
