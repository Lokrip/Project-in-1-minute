from django.shortcuts import render
from db.tasks import test_task

def index_app(request):
    test_task.delay()
    
    return render(
        request, 
        "base.html",
        dict(title = "Start Heroku!")
    )