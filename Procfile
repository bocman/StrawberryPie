web: gunicorn project.wsgi --log-file -
worker: celery -A project flower --broker=$REDIS_URL worker --beat -B --loglevel=info
