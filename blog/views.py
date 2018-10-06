from django.shortcuts import render
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

    