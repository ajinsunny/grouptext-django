# Django

[![Build status](https://badge.buildkite.com/50e41ba4d9bc98e4d9d4f04e0e551104dde8ab33f50a9ba80c.svg)](https://buildkite.com/dreamstate/grouptext-django)

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
