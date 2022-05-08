from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView
from django.db.models import Q




class SearchResultView(ListView):
    model = Post
    context_object_name = 'search_list'
    template_name = 'search/search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Post.published.filter(
            Q(title__icontains=query)| Q(description__icontains=query)
        )
        return object_list
