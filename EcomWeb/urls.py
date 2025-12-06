from django.urls import path, include
from django.contrib import admin
from ecomapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('spmodel', views.SpModel, basename='sp')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
