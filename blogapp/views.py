from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	
	return render(request, "index.html", context)

def detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	context = {'post': post}
	
	return render(request, "detail.html", context)