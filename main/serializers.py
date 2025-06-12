from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *

class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

class AlbumSafeSerializer(ModelSerializer):
    singer = SingerSerializer(read_only=True)
    class Meta:
        model = Album
        fields = '__all__'

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

