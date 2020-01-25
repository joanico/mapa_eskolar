from .views import MapPointView
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', MapPointView.as_view()),
]
