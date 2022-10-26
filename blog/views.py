from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    data = Post.objects.all()
    ctx = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'Postingan',
        'post': data
    }
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request=request, template_name='blog/blog.html', context=ctx)

# Create your views here.
