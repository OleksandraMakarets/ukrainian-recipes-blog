from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    Configuration for the 'blog' application.

    This class sets up the configuration for the 'blog' Django application,
    including specifying the default field type for automatically generated
    primary keys.

    **Attributes:**

    - `default_auto_field`: Specifies the default type of auto-generated
      primary keys for models in this application. Set to 'BigAutoField',
      which provides a 64-bit integer for primary keys.
    - `name`: The name of the application. This is used by Django to
      identify the application within the project.

    **Application Name:**
    
    - 'blog'
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
