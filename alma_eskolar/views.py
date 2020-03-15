from django.shortcuts import render
from .models import Subdistrict, EbcMap
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.serializers import serialize


class EbcmapListView(ListView):

    template_name = "base.html"
    model = EbcMap
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mappoints'] = serialize('geojson', EbcMap.objects.all(), geometry_field='geom')
        context['ebcmaps'] = EbcMap.objects.all()
        return context


class EbcmapDetailView(DetailView):

    model = EbcMap

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ebcmapas'] = EbcMap.objects.all()
        return context
