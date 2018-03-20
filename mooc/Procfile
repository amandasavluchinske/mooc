web: gunicorn theprojectname.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=theprojectname --loglevel=info
