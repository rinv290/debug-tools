from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path(
        'registration/',
        include('registration.urls')
    ),
    path(
        'api/',
        include('registration.api_urls')
    ),
    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()