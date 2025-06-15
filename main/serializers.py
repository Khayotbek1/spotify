from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import timedelta
from .models import *

class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'

class SingerNameSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = 'name'

class AlbumSafeSerializer(ModelSerializer):
    singer = SingerNameSerializer(read_only=True)
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

    def validate_file(self, file):
        if not str(file).lower().endswith('.mp3'):
            raise ValidationError('Only mp3 files are allowed')
        return file

    def validate_duration(self, duration):
        max_duration = timedelta(hours=0, minutes=7)
        if duration and duration > max_duration:
            raise ValidationError('Duration is too long, need 00:07:00 minutes')
        return duration

