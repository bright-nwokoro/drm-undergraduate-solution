from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('upload/', views.uploadView, name='upload'),
    path('you_cant_download_image/', views.noDownloadImageView, name='no_download_image'),
    path('you_cant_download_text/', views.noDownloadTextView, name='no_download_text'),
]
