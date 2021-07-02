from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request, 'drm_site/home.html', {})

def uploadView(request):
    return render(request, 'drm_site/upload.html', {})

def noDownloadImageView(request):
    return render(request, 'drm_site/dndownload_image.html', {})

def noDownloadTextView(request):
    return render(request, 'drm_site/dndownload_text.html', {})
