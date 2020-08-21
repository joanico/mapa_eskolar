from django.shortcuts import render
from .models import District, EbcMap 
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.serializers import serialize
from django.core.paginator import Paginator
from .forms import DistrictForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from .filters import EbcmapFilter

class EbcmapListView(ListView):

    template_name = "base.html"
    model = EbcMap
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['mappoints'] = serialize('geojson', EbcMap.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        context['filter'] =  EbcmapFilter(self.request.GET, queryset=self.get_queryset())
        return context


class EbcmapDetailView(DetailView):

    template_name = 'alma_eskolar/ebcmap_detail.html'
    model = EbcMap

    def get_context_data(self, *args, **kwargs):
        context = super(EbcmapDetailView, self).get_context_data(*args, **kwargs)
        ebc_pk = self.kwargs['pk']
        context['ebcmapas'] = EbcMap.objects.get(pk=ebc_pk)
        return context

