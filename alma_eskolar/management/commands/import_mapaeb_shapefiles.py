from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from ...models import MapPoint

class Command(BaseCommand):
    help = 'Import models from shapefiles'

    def handle(self, *args, **options):
        path_of_shp = './shapefiles/mapaeb.shp'
        mapaeb_mapping = {
            'name': 'name',
            'geom': 'Point'
        }
        try:
            lm = LayerMapping(MapPoint, path_of_shp, mapaeb_mapping, transform=True, unique=None, using=None)
            lm.save(strict=True, verbose=True)
            self.stdout.write(self.style.SUCCESS('Successfully imported Mapa EB'))
        except:
            raise CommandError('Error importing Mapa EB')
