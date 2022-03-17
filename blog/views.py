from django.shortcuts import render, get_object_or_404
from .models import Post, Category




def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.published.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
        return render(request, 'post/list.html', {'posts':posts,'category':category, 'categories':categories})
    else:
        context = {
            'posts':posts,
            'category': category,
            'categories': categories,

        }
        return render(request, 'post/list.html', context)



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'post/detail.html', context)
