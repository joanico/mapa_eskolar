from django.shortcuts import render
from .models import Subdistrict, EbcMap
from django.views.generic import TemplateView
from django.core.serializers import serialize


class EbcMapView(TemplateView):
    #kria template ba view nian
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, *kwargs)
        #get context ida ba map EBC nian.
        context['mappoints'] = serialize('geojson', EbcMap.objects.all(), geometry_field='geom')
        #get context ida ne'e ba lista eskola ebc
        context['ebcmaps'] = EbcMap.objects.all()

        return context
