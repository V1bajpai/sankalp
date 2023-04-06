
from django.urls import path, include

from content import views

urlpatterns = [
    path('video/', views.get_video_content),
    path('', views.get_news_content),
    path('home/', views.get_home_news),
    # path('news/latest/', views.get_latest_news),
    # path('news/sports/', views.get_sports_news),
    # path('news/election/', views.get_election_news),
    # path('news/entertainment/', views.get_entertainment_news),
    # path('news/technology/', views.get_technology_news),
    # path('news/business/', views.get_business_news),
    # path('news/education/', views.get_education_news),
]
