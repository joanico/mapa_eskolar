# Generated by Django 2.2.8 on 2020-02-01 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alma_eskolar', '0006_epmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epmap',
            name='name',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
