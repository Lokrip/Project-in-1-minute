web: SERVER_INSTANCE=web gunicorn app.service.wsgi --workers 2 --threads 4
release: python app/manage.py migrate && python app/manage.py collectstatic --noinput
