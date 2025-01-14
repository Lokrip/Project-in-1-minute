from django.shortcuts import render
from db.models import UserSummary
from .celery import update_total_time, test_task

def index_app(request):
    test_task.delay()
    summary, created = UserSummary.objects.get_or_create(user=request.user)
    
    if summary.total_time:
        total_time = summary.total_time
    else:
        total_time = 55
        update_total_time.delay(total_time, summary.id)
    
    return render(
        request, 
        "base.html",
        dict(title = "Start Heroku!", summary = summary)
    )