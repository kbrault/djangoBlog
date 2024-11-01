from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from datetime import datetime
import markdown 

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts, 'current_year': datetime.now().year})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, published_date__year=year, published_date__month=month, published_date__day=day)

    post.content_html = markdown.markdown(post.content)
    
    return render(request, 'blog/post_detail.html', {'post': post, 'current_year': timezone.now().year})