# Generated by Django 2.2.8 on 2020-01-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alma_eskolar', '0003_auto_20200122_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mappoint',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
