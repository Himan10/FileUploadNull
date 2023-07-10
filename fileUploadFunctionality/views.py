from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.conf import settings
from os.path import getsize
from django.template.loader import render_to_string

# Create your views here.
@login_required
def checkAuthentication(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = UserProfile.objects.get_or_create(user=user)
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
    context = {"message" : "", "success":  ""}
    if user_profile:
        # check some file validation and integrity
        if request.method == "POST":
            resume = request.FILES.get("resume")
            if resume:

                # check file size (shouldn't exceed 10mb)
                filesize = resume.size / (1024 * 1024) # in mb
                if (filesize > 10) :
                    context["message"] = "File size shouldn't exceed 10mb"
                    context["success"] = False
                else:
                    uploadFileToStorage = False
                    allowed_file_extensions = ["docx", "pdf", "doc"]
                    allowed_content_types = [
                        "application/pdf",
                        "application/msword",
                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    ]
                    fileExtension = resume.name.split(".")[1].lower()
                    if fileExtension in allowed_file_extensions and resume.content_type in allowed_content_types :
                        # check file signature thing
                        if fileExtension == "pdf":
                            if resume.file.read()[:4].hex().upper().encode("ASCII") == "25504446".encode("ASCII"):
                                uploadFileToStorage = True
                        elif fileExtension == "docx":
                            if resume.file.read()[:4].hex().upper().encode("ASCII") == '504B0304'.encode('ASCII'):
                                uploadFileToStorage = True
                        elif fileExtension == "doc":
                            if resume.file.read()[:4].hex().upper().encode("ASCII") == 'D0CF11E0A1B11AE1'.encode('ASCII'):
                                uploadFileToStorage = True
                        else:
                            context["message"] = "File type is not supported"
                            context["success"] = False

                # delete the existing one (default storage == MEDIA_ROOT)
                    if uploadFileToStorage:
                        if user_profile.resume:
                            default_storage.delete(user_profile.resume.path)
                        user_profile.resume = resume
                        user_profile.save()
    return render(request, "main.html", {"context" : context})

def fetch_resume(request):
    UserData = UserProfile.objects.get(user=request.user)
    return HttpResponse(UserData.resume.url)