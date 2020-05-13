# Django

# admin interface
https://grouptext-django.dreamstate-4-all.org/admin/
user=root
password=password123

# start/dev
$ docker-compose -f docker-compose.yml up

## Build project

```
docker-compose build
```

## Running for debug mode
```
docker-compose run --service web
```

## Start app
```
docker-compose run web python3 manage.py startapp <APPNAME>
```
