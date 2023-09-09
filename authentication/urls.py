from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('adminLogin', views.adminLogin, name='adminlogin'),
    path('image', views.image, name='image'),

    # path('logout', views.index, name='index'),
    

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)