from django.shortcuts import render
from rest_framework.decorators import api_view

from content import service


# Create your views here.


@api_view(['GET'])
def get_video_content(request, format=None):
    return service.get_all_videos(request)