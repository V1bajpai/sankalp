# from rest_framework import serializers
#
# from content.models import VideoContent, TextContent
#
#
# class VideoContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VideoContent
#         fields = "__all__"
#
#
#
# class TextContentSerializer(serializers.ModelSerializer):
#     # image_url = serializers.SerializerMethodField('get_image_url')
#     image = serializers.ImageField(use_url=True)
#
#     class Meta:
#         model = TextContent
#         fields = '__all__'
#
#     def get_image_url(self, obj):
#         return obj.image.url
#         # return self.context['request'].build_absolute_uri(obj.image.url)
