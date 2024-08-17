from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the :model:`About` model.

    This configuration uses the Summernote editor for the 'content' field.
    Summernote is a WYSIWYG editor that allows for rich text editing.

    **Attributes:**

    - `summernote_fields`: Specifies which fields should use the Summernote editor.
      Here, it is applied to the 'content' field.

    **Template Customization:**

    - This class inherits from `SummernoteModelAdmin` to integrate the Summernote editor.
      If you want to customize the admin panel view in your projects, you would 
      normally inherit from `admin.ModelAdmin`.
    """

    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the :model:`CollaborateRequest` model.

    This configuration displays specific fields in the admin list view.

    **Attributes:**

    - `list_display`: Specifies the fields to be displayed in the list view of the admin interface.
      Here, it includes 'message' and 'read'.

    **Note:**

    - This class inherits from `admin.ModelAdmin` for customizing the admin panel view.
    """

    list_display = ('message', 'read',)
