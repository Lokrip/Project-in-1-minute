from django.shortcuts import render

def index_app(request):
    return render(
        request, 
        "base.html",
        dict(title = "Start Heroku!")
    )