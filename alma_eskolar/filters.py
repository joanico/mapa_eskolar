import django_filters
from .models import EbcMap

class EbcmapFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = EbcMap
        fields = ['name', 'district']
