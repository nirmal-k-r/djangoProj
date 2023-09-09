from .models import Driver
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def status(request):
    return HttpResponse("Website is up and running")

def about(request):
    username="John"
    ctx = {  #context contains all the variables and objects that you want to render the template with 
        'username': username
    }
    template = loader.get_template('polls/about.html')
    return HttpResponse(template.render(ctx, request))


def drivers(request):

    ctx={
        'drivers': Driver.objects.all().order_by('id')
    }
    
    
    template = loader.get_template('polls/drivers.html')
    return HttpResponse(template.render(ctx, request))
