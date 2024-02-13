from django.contrib import admin
from django.urls import path 
from .views import information_form_view
from .views import success_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('info/',information_form_view,name='info'),
  path('success/', success_view, name='success'),
  path('admin/', admin.site.urls)
  
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
