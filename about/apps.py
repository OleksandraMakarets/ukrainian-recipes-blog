from django.apps import AppConfig

class AboutConfig(AppConfig):
    """
    Configuration for the 'about' application.

    This class configures the 'about' Django application and specifies
    the default field type for automatically generated primary keys.

    **Attributes:**

    - `default_auto_field`: Specifies the default type of auto-generated
      primary keys for models in this application. Set to 'BigAutoField',
      which provides a 64-bit integer for primary keys.
    - `name`: The name of the application. This is used by Django to
      identify the application in the project.

    **Application Name:**
    
    - 'about'
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
