import traceback

from starlette.responses import JSONResponse

from content.models import VideoContent, TextContent
from rest_framework import status
from rest_framework.response import Response
from fastapi_admin.i18n import _

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
