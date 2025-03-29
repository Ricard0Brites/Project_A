
from urllib.request import Request

from django.urls import path

from . import views
# Admin App URLS

urlpatterns = \
[
    path('', views.entrypoint),
]