from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    # Get the post object or 404 if not found
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # Add success message
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            # Redirect to the same post detail page to avoid resubmission on refresh
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def profile_page(request):
    """
    Display the profile page of the currently logged-in user.

    **Context**

    ``user``
        An instance of :model:`auth.User`.
    ``comments``
        A queryset of comments made by the user.

    **Template:**

    :template:`profile_page.html`
    """
    # Get the currently logged-in user
    user = get_object_or_404(User, pk=request.user.pk)
    # Get all comments made by the user
    comments = user.comments.all()

    # Prepare context for rendering
    context = {
        'user': user,
        'comments': comments,
    }

    return render(request, 'profile_page.html', context)

