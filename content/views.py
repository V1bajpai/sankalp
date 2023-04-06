from django.shortcuts import render
from rest_framework.decorators import api_view

from content import service


# Create your views here.


@api_view(['GET'])
def get_video_content(request, format=None):
    return service.get_all_videos(request)

@api_view(['GET'])
def get_news_content(request, format=None):
    return service.get_all_news(request)

@api_view(['GET'])
def get_home_news(request, format=None):
    return service.get_home_news(request)

# @api_view(['GET'])
# def get_latest_news(request, format=None):
#     return service.get_latest_news(request)
#
# @api_view(['GET'])
# def get_sports_news(request, format=None):
#     return service.get_sports_news(request)
#
# @api_view(['GET'])
# def get_election_news(request, format=None):
#     return service.get_election_news(request)
#
# @api_view(['GET'])
# def get_entertainment_news(request, format=None):
#     return service.get_entertainment_news(request)
#
# @api_view(['GET'])
# def get_technology_news(request, format=None):
#     return service.get_technology_news(request)
#
# @api_view(['GET'])
# def get_business_news(request, format=None):
#     return service.get_business_news(request)
#
# @api_view(['GET'])
# def get_education_news(request, format=None):
#     return service.get_education_news(request)