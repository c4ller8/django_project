from django.contrib import admin
from .models import Episode


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('episode_number', 'title', 'image_url')
    list_filter = ('episode_number',)
    search_fields = ('title', 'description')
