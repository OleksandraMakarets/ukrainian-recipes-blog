from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form for submitting collaboration requests.

    This form is linked to the :model:`CollaborateRequest` model and allows
    users to input their name, email, and a message to request collaboration.

    **Fields:**

    - `name`: The name of the person requesting collaboration.
    - `email`: The email address of the person requesting collaboration.
    - `message`: The message or details about the collaboration request.

    This form automatically handles validation and saving of these fields
    to the database.
    """

    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
