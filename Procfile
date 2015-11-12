web: gunicorn project.wsgi --log-file -
worker: celery -A project flower --broker=$REDIS_URL --db=$DATABASE_URL worker --beat -B --loglevel=info
