from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the :model:`Post` model.

    This configuration uses the Summernote editor for specified fields
    and includes various customizations for the admin interface.

    **Attributes:**

    - `list_display`: Specifies the fields to be displayed in the list view of the admin interface.
      Includes 'title', 'slug', 'status', 'cooking_time', and 'created_on'.
    - `search_fields`: Defines which fields should be searchable in the admin interface.
      Includes 'title', 'content', 'ingredients', and 'instructions'.
    - `list_filter`: Sets up filters in the admin interface for quick data sorting.
      Includes 'status', 'created_on', and 'cooking_time'.
    - `prepopulated_fields`: Automatically populates the 'slug' field based on the 'title'.
    - `summernote_fields`: Specifies which fields should use the Summernote WYSIWYG editor.
      Includes 'content', 'ingredients', and 'instructions'.

    **Note:**

    - This class inherits from `SummernoteModelAdmin` to integrate the Summernote editor,
      providing rich text editing capabilities. For standard admin customization, you would
      normally inherit from `admin.ModelAdmin`.
    """

    list_display = ('title', 'slug', 'status', 'cooking_time', 'created_on')
    search_fields = ['title', 'content', 'ingredients', 'instructions']
    list_filter = ('status', 'created_on', 'cooking_time',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingredients', 'instructions',)

# Register the Comment model with the default admin interface
admin.site.register(Comment)
