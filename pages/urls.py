from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:page_id>', views.page, name='blog'),
]

