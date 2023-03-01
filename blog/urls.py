from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('postComment', views.postComment, name='postComment'),
    path('createblog', views.createblog, name='createblog'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]