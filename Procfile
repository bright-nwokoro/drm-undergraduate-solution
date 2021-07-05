web: gunicorn drm_systen.drm_systen.wsgi --log-file -
web: python drm_systen/manage.py makemigrations
web: python drm_systen/manage.py migrate
web: python drm_systen/manage.py runserver 0.0.0.0:$PORT
