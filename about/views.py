from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):
    """
    Handles the 'About Me' page view.

    If the request method is POST, the function processes the submitted
    collaboration form, validates it, and if valid, saves the form data
    and displays a success message to the user.

    Retrieves the latest 'About' entry from the database based on the
    'updated_on' timestamp, and initializes an empty 'CollaborateForm'
    for use in the page.

    Renders the 'about.html' template with the retrieved 'about' entry
    and the collaboration form.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse object with the rendered 'about/about.html' template
      and context containing the 'about' entry and 'collaborate_form'.
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
