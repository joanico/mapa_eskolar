from django.db import models
from django.contrib.gis.db import models
from django.urls import reverse

#Model ba Mapa Sub-distrito nia 
class Subdistrict(models.Model):
    name = models.CharField(max_length=124)

    geom = models.MultiPolygonField()

    def __str__(self):
        return '{} pk:{}'.format(self.name, self.pk)

#Model ba Mapa Eskola EBC nian
class EbcMap(models.Model):
    name = models.CharField(max_length=100, blank=True)
    geom = models.PointField()
    description = models.TextField(max_length=None, blank=True)

    def get_absolute_url(self):
        return reverse('ebcmap-detail', args=[str(self.id)])

    def __str__(self):
        return '{} geom:{}'.format(self.name, self.geom)

#Model ba Mapa Eskola Pre-Eskolar
class EpMap(models.Model):
    name = models.CharField(max_length=254, blank=True)
    geom = models.PointField()
    description = models.TextField(max_length=None, blank=True)

    def __str__(self):
        return '{} geom:{}'.format(self.name, self.geom)