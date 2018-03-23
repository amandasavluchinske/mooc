web: gunicorn mooc.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=mooc --loglevel=info
