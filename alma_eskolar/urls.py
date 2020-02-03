from .views import EbcmapListView, EbcmapDetailView
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', EbcmapListView.as_view(), name='ebcmap-list'),
    path('ebcmap/<int:pk>/', EbcmapDetailView.as_view(), name='ebcmap-detail'),
]
