from django.contrib import admin
from .models import Song

# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'duration')
    list_filter = ('artist',)
    search_fields = ('title', 'artist')
    ordering = ('title',)
