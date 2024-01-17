from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# Create your views here.
class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 3 # adds a paginator and a page_obj to the context
    template_name='pages/index.html'
    
'''   
def index(request):
    blogs = Blog.objects.all()
    paaginator = Paginator(blogs, 3)
    
    return render(request, 'pages/index.html', {'blogs':blogs})
'''
def page(request, page_id):
    blog = get_object_or_404(Blog, pk=page_id)
    return render(request, 'pages/blog.html', {'blog':blog})

def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pages:index')
    else:
        form = BlogForm()
        context = {'form':form}
        return render(request, 'pages/blog_add.html', context)



