from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow World")

def about(request):
    return HttpResponse("Hellow ABout")
