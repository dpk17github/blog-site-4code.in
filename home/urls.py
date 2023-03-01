from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('search', views.search, name='search'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('handlelogin', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('myprofile', views.myprofile, name='myprofile'),
]