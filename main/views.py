from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello World hola")

def about(request):
    return HttpResponse("About")