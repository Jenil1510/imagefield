# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Information

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'salary', 'display_thumbnail']

    def display_thumbnail(self, obj):
        if obj.img:
            return format_html('<img src="{}" class="image-preview" width="100" height="100" />', obj.img.url)
        return 'No Image'

    display_thumbnail.short_description = 'Thumbnail'
