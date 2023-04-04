
from django.urls import path, include

from content import views

urlpatterns = [
    path('video/', views.get_video_content),
]
