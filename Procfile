web: SERVER_INSTANCE=web gunicorn service.wsgi:application --workers 2 --threads 4
release: python app/manage.py migrate && python app/manage.py collectstatic --noinput
