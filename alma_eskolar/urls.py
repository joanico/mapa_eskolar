from .views import EbcMapView
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', EbcMapView.as_view()),
]
