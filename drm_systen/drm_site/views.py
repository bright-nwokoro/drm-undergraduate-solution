from django.shortcuts import render
from .forms import *

# Create your views here.

def homeView(request):
    return render(request, 'drm_site/home.html', {})

def uploadView(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'drm_site/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'drm_site/upload.html', {'form': form})

def noDownloadImageView(request):
    return render(request, 'drm_site/dndownload_image.html', {})

def noDownloadTextView(request):
    return render(request, 'drm_site/dndownload_text.html', {})
