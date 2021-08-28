from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/v1/chat/', include('fastzap.chat.urls')),
    path('chat/', include('fastzap.website.urls')),
]
