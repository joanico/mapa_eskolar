from django.shortcuts import render
from .models import Subdistrict, Subdistrict, MapPoint
from django.views.generic import TemplateView
from django.core.serializers import serialize


class MapPointView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, *kwargs)

        context['mappoints'] = serialize('geojson', MapPoint.objects.all(), geometry_field='geom')

        return context

