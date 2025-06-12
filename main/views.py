from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class SingersAPIView(APIView):
    def get(self,request):
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumsAPIView(APIView):
    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSafeSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongsAPIView(APIView):
    def get(self,request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    