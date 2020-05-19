from .views import EbcmapListView, EbcmapDetailView
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', EbcmapListView.as_view(), name='ebcmap-list'),
    path('ebcmap/<int:pk>/', EbcmapDetailView.as_view(), name='ebcmap-detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
