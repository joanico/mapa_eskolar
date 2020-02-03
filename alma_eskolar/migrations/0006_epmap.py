# Generated by Django 2.2.8 on 2020-01-31 14:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alma_eskolar', '0005_auto_20200131_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]