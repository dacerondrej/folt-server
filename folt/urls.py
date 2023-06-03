from django.contrib import admin
from django.urls import path, include
from folt_api import urls as folt_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('folt/', include(folt_urls)),
]
