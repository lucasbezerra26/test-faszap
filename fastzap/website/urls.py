from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:attendance>/', roomClient, name='room'),
    path('atendente/<int:attendance>/', roomAtendace, name='room'),
]

