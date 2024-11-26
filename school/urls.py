

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin

# Importiraj svoje poglede (views)
from education import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Dodaj druge URL-ove
]

# Dodaj statičke datoteke za razvojno okruženje
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
