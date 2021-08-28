from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'clients', ClientViewSet)
router.register(r'attendaces', AttendanceViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("message/<int:attendance>/", MessageFilterViewSet.as_view()),
    path("client/attendaces/<int:client>/", AttendanceFilterViewSet.as_view()),

]

