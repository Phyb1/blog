from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pages'
urlpatterns = [
    path('', views.BlogList.as_view() , name='index'),
    path('<int:page_id>/', views.page, name='blog'),
    path('add/', views.blog_add, name='blog_add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

