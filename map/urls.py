from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("markers/", views.MarkerView.as_view()),
    path("markers/<int:pk>/", views.MarkerDetailView.as_view()),
]
