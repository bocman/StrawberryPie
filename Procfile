web: gunicorn project.wsgi --log-file -
worker: celery -A project worker --beat -B --loglevel=info

