# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

# ========== FUNCTION-BASED VIEWS ============
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "home.html", {"posts": posts})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "post_detail.html", {"post": post})


# ========== GENERIC CLASS-BASED VIEWS ==============
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
