from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/index.html', {'blogs':blogs})

def page(request, page_id):
    blog = get_object_or_404(Blog, pk=page_id)
    return render(request, 'pages/blog.html', {'blog':blog})
