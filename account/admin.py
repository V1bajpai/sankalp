from django.contrib import admin

from account.models import UserDetail
from content.models import VideoContent, TextContent

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(VideoContent)
# admin.site.register(TextContent)
# admin.site.unregister(PasswordResetTokens)