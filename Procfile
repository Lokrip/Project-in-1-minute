web: SERVER_INSTANCE=web gunicorn service.service.wsgi --workers 2 --threads 4
release: python service/manage.py migrate && python service/manage.py collectstatic --noinput
