import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()



@app.task
def update_total_time(total_time, summary_id):
    from db.models import UserSummary
    summary = UserSummary.objects.get(id=summary_id)
    summary.total_time = total_time
    summary.save()
    

@app.task
def test_task():
    print('yes!!')