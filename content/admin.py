from django.contrib import admin

from content.models import TextContent

# Register your models here.
# admin.site.register(TextContent)
@admin.register(TextContent)
class TextContent(admin.ModelAdmin):
    list_display = ['id','image']