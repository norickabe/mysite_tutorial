import http
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from todo.models import Post
#from todo.forms import PostForm

# Create your views here.

def top(request) -> HttpResponse:
    return render(request, 'top.html')

def post_list(request) -> render:
    all_posts = Post.objects.all().order_by('id')
    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'todo/post_list.html', {'posts': posts})

def post_edit(request, post_id=None) -> render:
    if post_id:
        post = get_object_or_404(Post, pk=post_id)
    else:
        post = Post()

    if request.method() == 'POST':
        form = PostForm()


