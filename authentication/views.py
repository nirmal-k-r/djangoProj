from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

from .forms import LoginForm,AdminLoginForm,imageForm
from .models import imageModel



# Create your views here.
def index(request):
    ctx={
        
    }
    template = loader.get_template('auth/index.html')
    return HttpResponse(template.render(ctx, request))

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['username']=='admin' and form.cleaned_data['password']=='12345':
               return HttpResponse(f'welcome {form.cleaned_data["username"]}') #instead redirect to dashboard
            else:
                return HttpResponse('wrong username or password')

    return HttpResponse('wrong request')

def adminLogin(request):
    if request.method == 'GET':
        ctx={
            'form':AdminLoginForm(),
            'url': AdminLoginForm.url
        }
        template = loader.get_template('auth/adminLogin.html')
        return HttpResponse(template.render(ctx, request))
        

    elif request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['username']=='admin' and form.cleaned_data['password']=='12345':
               return HttpResponse(f'welcome {form.cleaned_data["username"]}') #instead redirect to dashboard
            else:
                return HttpResponse('wrong username or password')  
    return HttpResponse('wrong request')


def image(request):
    if request.method == 'GET':
        ctx={
            'form': imageForm()
        }
        template = loader.get_template('auth/image.html')
        return HttpResponse(template.render(ctx, request))
    
    elif request.method == 'POST':
        form = imageForm(request.POST,request.FILES)
        img=form.cleaned_data['image']
        if form.is_valid():
            imageFile=imageModel(image=img)
            imageFile.save()
            return HttpResponse('image uploaded')