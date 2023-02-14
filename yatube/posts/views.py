from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import PostForm
from .models import Post, Group

User = get_user_model()


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': author,
        'username': username
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse('posts:post_detail', request.user))
    form = PostForm()
    context = {'form': form}
    return render(request, 'posts/create_post.html', context)


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.id != post.author.id:
        return redirect("posts/<int:post_id>/", post.post_id)
    form = PostForm(instance=post)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("posts:post_detail", post.id)
    context = {
        "form": form,
        "is_edit": True,
    }
    return render(request, "posts/create_post.html", context)
