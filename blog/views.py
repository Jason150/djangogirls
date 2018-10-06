from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.filter()\
        .order_by('published_date')
    return render(
        request,
        'post_list.html',
        {'contents': posts}
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        'post_detail.html',
        {'content': post}
    )

    