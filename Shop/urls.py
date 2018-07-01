from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^', include('landing.urls')),
    url(r'admin/', admin.site.urls)
]\
    + static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS) \
    + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
