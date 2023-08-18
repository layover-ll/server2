from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("map/", include("map.urls")),
    path('user/', include('accounts.urls')),
    path("healthcheck", views.HealthCheck.as_view()),
]
