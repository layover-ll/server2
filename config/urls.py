from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("map/", include("map.urls")),
    path('user/', include('accounts.urls')),
]