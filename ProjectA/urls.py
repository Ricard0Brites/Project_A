from django.contrib import admin
from django.urls import include, path
from ProjectA.Apps.Core import urls as core_urls
from ProjectA.Apps.Admin import urls as admin_urls

# Main URLS

urlpatterns = [
    path('', include(admin_urls)),
    path('admin/', admin.site.urls),
]