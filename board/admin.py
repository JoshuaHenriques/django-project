from django.contrib import admin
from .models import Post, Comment


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', 'slug')
    prepopulated_fields = {'slug': ('title', )}


# Register your models here.
admin.site.register(Post, BoardAdmin)
admin.site.register(Comment)
