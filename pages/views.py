from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/index.html', {'blogs':blogs})

def page(request, page_id):
    blog = get_object_or_404(Blog, pk=page_id)
    return render(request, 'pages/blog.html', {'blog':blog})

def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:index')
    else:
        form = BlogForm()
        context = {'form':form}
        return render(request, 'pages/blog_add.html', context)



