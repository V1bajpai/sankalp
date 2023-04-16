import traceback

from starlette.responses import JSONResponse

from content.models import VideoContent, TextContent
from rest_framework import status
from rest_framework.response import Response
from fastapi_admin.i18n import _

# from content.serializers import TextContentSerializer


def get_all_videos(request):
    try:
        video_content = VideoContent.objects.all().values()
        return Response({'content': video_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_all_news(request):
    try:
        news_content = TextContent.objects.all().values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)


    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_home_news(request):
    try:
        news_content = TextContent.objects.filter(category='Home').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_latest_news(request):
    try:
        news_content = TextContent.objects.filter(category='Latest').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_sports_news(request):
    try:
        news_content = TextContent.objects.filter(category='Sports').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_election_news(request):
    try:
        news_content = TextContent.objects.filter(category='Election').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_entertainment_news(request):
    try:
        news_content = TextContent.objects.filter(category='Entertainment').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_technology_news(request):
    try:
        news_content = TextContent.objects.filter(category='Technology').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_business_news(request):
    try:
        news_content = TextContent.objects.filter(category='Business').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def get_education_news(request):
    try:
        news_content = TextContent.objects.filter(category='Education').values()
        return Response({'content': news_content}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)