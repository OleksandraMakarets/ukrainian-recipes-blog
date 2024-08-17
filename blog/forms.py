from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on blog posts.

    This form is linked to the :model:`Comment` model and allows users
    to input the content of their comment.

    **Fields:**

    - `body`: The text content of the comment.

    This form automatically handles validation and saving of the comment
    content to the database.
    """

    class Meta:
        model = Comment
        fields = ('body',)
