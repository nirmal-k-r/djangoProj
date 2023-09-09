from django.contrib import admin

# Register your models here.
from .models import Submarine, Driver
admin.site.register(Submarine)
admin.site.register(Driver)
