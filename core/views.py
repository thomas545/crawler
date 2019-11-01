from django.shortcuts import render
from .serializers import YoutubeSerializer
from .models import Youtube
from rest_framework import views, generics, exceptions, exceptions, permissions
from rest_framework.response import Response
from .crawler import CrawlerChannel, CrawlerPlayList
import json


class ListYouTubeVideosView(generics.ListCreateAPIView):
    serializer_class = YoutubeSerializer
    queryset = Youtube.objects.all()

    def create(self, request, *args, **kwargs):
        data = json.loads(CrawlerChannel)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)