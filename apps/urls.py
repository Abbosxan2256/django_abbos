# from django.contrib import admin
from django.urls import path, include

from apps.views import index_prc

urlpatterns = [
    path('', index_prc, name='index_prc'),
]





















