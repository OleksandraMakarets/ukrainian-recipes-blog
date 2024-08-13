from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'cooking_time', 'created_on')
    search_fields = ['title', 'content', 'ingredients', 'instructions']
    list_filter = ('status', 'created_on', 'cooking_time',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingredients', 'instructions',)

# Register your models here.
admin.site.register(Comment)
