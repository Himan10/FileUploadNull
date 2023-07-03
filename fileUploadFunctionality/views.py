from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.conf import settings

# Create your views here.
@login_required
def checkAuthentication(request):
    if request.user.is_authenticated:
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        user_profile = UserProfile.objects.get(user=user)
        return user_profile
    return False

# this view displays a string on the frontend
@login_required
def main(request):
    user_profile = checkAuthentication(request)
    if (user_profile):
        return render(request, "main.html", {"img": user_profile.profile_image.url})
    return HttpResponse("User is not authenticated")

def sayhello(request):
    print(request)
    return render(request, "helloNULL.html")

def upload_image(request):
    user_profile = checkAuthentication(request)
    if (user_profile) :
        if request.method == 'POST':
            print(user_profile)
            image = request.FILES.get('profile_picture')
            if image:
                if user_profile.profile_image:
                    default_storage.delete(user_profile.profile_image.path)
                user_profile.profile_image = image
                user_profile.save()
        return render(request, 'main.html', {"img": user_profile.profile_image.url})
    return HttpResponse("User is not authenticated")

def upload_file(request):
    user_profile = checkAuthentication(request)
    if user_profile:
        if request.method == "POST":
            resume = request.FILES.get("resume")
            if resume:
                # delete the existing one (default storage == MEDIA_ROOT)
                if user_profile.resume:
                    default_storage.delete(user_profile.resume.path)
                user_profile.resume = resume
                user_profile.save()
    return render(request, "main.html")

def fetch_resume(request):
    UserData = UserProfile.objects.get(user=request.user)
    return HttpResponse(UserData.resume.url)