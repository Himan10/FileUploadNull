from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this view displays a string on the frontend
def main(request):
    return render(request, "main.html")