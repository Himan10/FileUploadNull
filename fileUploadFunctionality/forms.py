# This class is responsible for form handling, validation and other stuff

from django import forms

class DisplayPictureForm(forms.Form):
    profile_picture = forms.ImageField()
    print(profile_picture)
