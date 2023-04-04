from rest_framework import serializers

from content.models import VideoContent


class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = "__all__"