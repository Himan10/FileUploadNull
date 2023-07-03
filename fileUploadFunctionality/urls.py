# This file is necessary in order to route the request to specific views
# path from django.urls is a function that takes two params, where the 
# first param is the path in url, and another is the view that's going to be used for that specific

from django.urls import path
from . import views
from .views import checkAuthentication

# URLConf
urlpatterns = [
    path('main/', views.main, name="main"),
    path('update/', views.upload_image, name='uploadImage'),
    path('resume-upload/', views.upload_file, name="uploadFile"),
    path('fetch-resume/', views.fetch_resume, name="viewResume")
]