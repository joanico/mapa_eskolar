from django.shortcuts import render
from .models import District, EbcMap
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.serializers import serialize
from django.core.paginator import Paginator


class EbcmapListView(ListView):

    template_name = "base.html"
    model = EbcMap
    paginate_by = 10  # if pagination is desired
    queryset = EbcMap.objects.all()  # Default: Model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mappoints'] = serialize('geojson', EbcMap.objects.all(), geometry_field='geom')
        context['districts'] = serialize('geojson', District.objects.all(), geometry_field='geom')
        return context

class EbcmapDetailView(DetailView):

    template_name = 'alma_eskolar/ebcmap_detail.html'
    model = EbcMap

    def get_context_data(self, *args, **kwargs):
        context = super(EbcmapDetailView, self).get_context_data(*args, **kwargs)
        context['ebcmapas'] = EbcMap.objects.all()
        return context


def listing(request):
    ebcmap_list = EbcMap.objects.all()
    paginator = Paginator(ebcmap_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'base.html', {'pape_obj': page_obj})
