web: gunicorn project.wsgi --log-file -
worker: celery flower -A project worker --beat -B --loglevel=info --broker=redis://h:pcaq1skmhhbgou5qk6t63iqik96@ec2-54-195-242-227.eu-west-1.compute.amazonaws.com:7739//

