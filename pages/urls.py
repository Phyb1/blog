from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:page_id>/', views.page, name='blog'),
    path('add/', views.blog_add, name='blog_add'),
]

