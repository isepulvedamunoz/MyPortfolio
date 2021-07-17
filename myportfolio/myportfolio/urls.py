
from django.contrib import admin
from django.urls import path

from django.config import settings
from django.config.urls.static import static

from main_page import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
