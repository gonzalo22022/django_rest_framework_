
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import TestView
from django.conf.urls.static import static



urlpatterns = [
    path('test/',TestView.as_view()),
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
