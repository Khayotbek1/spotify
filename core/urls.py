from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf import settings
from main.views import *

router = DefaultRouter()
router.register('albums', AlbumsViewSet)
router.register('singers', SingersViewSet)
router.register('songs', SongsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
