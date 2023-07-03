from django.db import models
from django.contrib.auth.models import User
from django.contrib.staticfiles.storage import staticfiles_storage
from testingFileUploadNULL.settings import BASE_DIR
from os.path import join

# Create your models here.
def defaultImagePath():
    return 'media/pp-armor.jpg'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_pictures/", default=defaultImagePath())
    resume = models.FileField(upload_to="resume/", default=None, null=True)
    resume_file_path = models.CharField(max_length=255, blank=True)


    def save(self, *args, **kwargs):
        if self.resume:
            self.resume_file_path = self.resume.path
        else:
            self.resume_file_path = ""
        super().save(*args, **kwargs)