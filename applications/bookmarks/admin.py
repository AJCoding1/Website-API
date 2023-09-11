from django.contrib import admin
from .models import Bookmark



class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user','post','created_at']
    list_display_links = ['user','post','created_at']


admin.site.register(Bookmark, BookmarkAdmin)
