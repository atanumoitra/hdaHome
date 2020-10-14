from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home_screen_view(request):
	return render(request, "hda/home.html", {})