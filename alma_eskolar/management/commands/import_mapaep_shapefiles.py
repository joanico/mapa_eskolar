from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from ...models import EpMap

class Command(BaseCommand):
    help = 'Import models from shapefiles'

    def handle(self, *args, **options):
        path_of_shp = './shapefiles/mapa_ep/mapa_ep.shp'
        mapaep_mapping = {
            'name': 'name',
            'geom': 'Point'
        }
        lm = LayerMapping(EpMap, path_of_shp, mapaep_mapping, encoding='latin-1', transaction_mode='autocommit', transform=True, unique=None, using='default')
        lm.save(strict=True, verbose=True)
        self.stdout.write(self.style.SUCCESS('Successfully imported Mapa EP'))
