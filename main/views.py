from django.contrib.admin import action
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# class SingersAPIView(APIView):
#     def get(self,request):
#         singers = Singer.objects.all()
#         serializer = SingerSerializer(singers, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = SingerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingersViewSet(ModelViewSet):
    serializer_class = SingerSerializer
    queryset = Singer.objects.all()

    @action(detail=True, methods=['GET'])
    def albums(self, request, pk):
        singer = get_object_or_404(Singer, pk=pk)
        albums = Album.objects.filter(singer=singer)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


class AlbumsViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    @action(detail=True, methods=['GET'])
    def songs(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        songs = Song.objects.filter(album=album)
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)



# class SongsAPIView(APIView):
#     def get(self,request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = SongSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongsViewSet(ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    @action(detail=True, methods=['GET'])
    def singer(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        singer = song.album.singer
        serializer = SingerSerializer(singer)
        return Response(serializer.data)

