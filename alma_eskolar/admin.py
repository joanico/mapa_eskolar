from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import EpMap, EbcMap, Subdistrict

#Set leaflet map iha admin tuir coordinator nebe fo ona iha nee
settings_overrides =  {
    'DEFAULT_CENTER': ([-8.8315139, 125.6199236,8]),
    'DEFAULT_ZOOM': 7,
}

class SubdistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']

admin.site.register(Subdistrict, SubdistrictAdmin)
admin.site.register(EbcMap, LeafletGeoAdmin)
admin.site.register(EpMap, LeafletGeoAdmin)
