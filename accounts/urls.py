from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
 ]