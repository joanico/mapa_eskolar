# mapa_eskolar
Kria mapa eskola sira iha Timor Leste 
## Etepa kria mapa eskolar

1. Setup enviroment

   - `mkdir mapa_eskolar`
   - cd `maka_eskolar`
   - `pyenv virtualenv mapa_eskolar`
   - `pyenv local`

2. kria project

3. `pip install django`

4. `django-admin startproject maka_eskolar`

5. `cd maka_eskolar`

6. `./manage startapp alma_eskolar`

7. Setup app iha setting INSTALLED_APPS `alma_eskolar`

8. install postgresql no kria database ho posgis

   - `pip install psycopg2`

   - `createdb mapa_eskolardb`

   - kria postgis extension

     `psql mapa_eskolardb`

     `CREATE EXTENSION postgis;`

   - konfigura database iha settings

     ```
     DATABASES = {
         'default': {
             'ENGINE': 'django.contrib.gis.db.backends.postgis',
             'NAME': 'mapa_eskolardb',
         }
     }
     ```
9. Rejistu postgis iha `INSTALLED_APPS` settings `django.contrib.gis`

10. Extra file mapa eskolar ho .shp husi shapefiles no uza funsaun `ogeinfo`
       - `ogrinfo shapefiles/mapaeb.shp`  

       - `ogrinfo -so shapefiles/mapaeb.shp mapaeb`
11. Kria model 
12. setup admin
13. `./manage.py makemigrations` 
14. `./manage.py sqlmigrate alma_eskolar 0001`

             BEGIN;
             --
             -- Create model MapPoint
             --
             CREATE TABLE "alma_eskolar_mappoint" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "geom" geometry(POINT,4326) NOT NULL, "description" text NOT NULL);
             CREATE INDEX "alma_eskolar_mappoint_geom_id" ON "alma_eskolar_mappoint"USING GIST ("geom");
             COMMIT;

15. `./manage.py migrate `

                 Operations to perform:
               Apply all migrations: admin, alma_eskolar, auth, contenttypes, sessions
                 Running migrations:
                   Applying alma_eskolar.0001_initial... OK

16.  Kria Surperuser `./manage.py createsuperuser`
17. Run server `./manage.py runserver`
18. Loke admin hodi hare rezultadu iha admin.
19. Etapa tuir kria view ho template hodi hare rezultadu iha interface
20. Kria View.py
21. Kria urls.py iha apps
22. kria urls.py project
23. kria template
24. konfigura leaflet map iha settings
           ```
           LEAFLET_CONFIG = {
               # conf here
               'DEFAULT_CENTER': (-8.801, 126.159),
               'DEFAULT_ZOOM': 16,
               'MIN_ZOOM': 2,
               'MAX_ZOOM': 10,
           }
           ```
25. Hatama css ba static
26. konfigura file static iha settings
           ```
           STATIC_URL = '/static/'
               
               STATICFILES_DIRS = [
                   os.path.join(BASE_DIR, "alma_eskolar/static"),
               ]
           ```
27. Reload pajina hodi hare ita nia mapa     
Reference: 
   Django Filter :
   
   Django pagination : https://dj-pagination.readthedocs.io/en/latest/usage.html
   
   Combination of django filter and pagination: https://github.com/carltongibson/django-filter/issues/13
