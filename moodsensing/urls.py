
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .routers import router
from core import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('HappyPlaces/', include('core.urls')),
    path('stats/', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

