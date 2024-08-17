from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    ``comments``
        A queryset of approved comments related to the post.
    ``comment_count``
        The total number of approved comments for the post.
    ``comment_form``
        A form instance for submitting a new comment.

    **Template:**

    :template:`blog/post_detail.html`
    """

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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
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

def comment_edit(request, slug, comment_id):
    """
    Handles editing an existing comment.

    This view allows a user to edit their own comment on a blog post.
    If the comment is successfully updated, it is marked as not approved
    until re-moderated.

    **Parameters:**

    - `request`: The HTTP request object.
    - `slug`: The slug of the blog post related to the comment.
    - `comment_id`: The ID of the comment to be edited.

    **Returns:**

    - A redirect to the post detail page after the comment is edited
      or if there was an error during editing.
    """

    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Handles deleting a comment.

    This view allows a user to delete their own comment on a blog post.
    If the comment is successfully deleted, a success message is displayed.
    If the user tries to delete a comment they do not own, an error message is shown.

    **Parameters:**

    - `request`: The HTTP request object.
    - `slug`: The slug of the blog post related to the comment.
    - `comment_id`: The ID of the comment to be deleted.

    **Returns:**

    - A redirect to the post detail page after the comment is deleted or
      if there was an error during deletion.
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

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

    user = get_object_or_404(User, pk=request.user.pk)
    comments = user.comments.all()

    context = {
        'user': user,
        'comments': comments,
    }

    return render(request, 'profile_page.html', context)


