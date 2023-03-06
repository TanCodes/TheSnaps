"""thesnaps URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . views import search_by_title, show_index_page , show_category , home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', show_index_page),
    path('home/search/', search_by_title),
    path('',home),
    path('category/<int:cid>/', show_category),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)