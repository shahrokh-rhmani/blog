from django.shortcuts import render, get_object_or_404
from .models import Post




def post_list(request):
    posts = Post.published.all()

    context = {
        'posts':posts,
    }
    return render(request, 'post/list.html', context)



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post':post,
    }

    return render(request, 'post/detail.html', context)
