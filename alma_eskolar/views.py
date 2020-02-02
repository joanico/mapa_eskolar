from django.shortcuts import render
from .models import Subdistrict, EbcMap
from django.views.generic import TemplateView
from django.core.serializers import serialize


class EbcMapView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, *kwargs)

        context['mappoints'] = serialize('geojson', EbcMap.objects.all(), geometry_field='geom')
        context['ebcmaps'] = EbcMap.objects.all()

        return context
