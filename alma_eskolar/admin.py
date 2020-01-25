from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import MapPoint, Subdistrict

#admin.site.register(Point, LeafletGeoAdmin)
class SubdistrictAdmin(admin.OSMGeoAdmin):
    list_display = ['name']
    list_filter = ['name']

admin.site.register(Subdistrict, SubdistrictAdmin)
admin.site.register(
    MapPoint,                      #<-- this is a model
    LeafletGeoAdmin,
    settings_overrides =  {
        'DEFAULT_CENTER': ([-8.8315139, 125.6199236,8]),
        'DEFAULT_ZOOM': 8,
    }
)
