from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Artist, Album

class ArtistSerializer(HyperlinkedModelSerializer):
    albums = serializers.HyperlinkedRelatedField(view_name='album-detail', many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'bio', 'albums')

class AlbumSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'year')
