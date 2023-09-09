from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save

# Create your models here.

class Submarine(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    year=models.IntegerField()
    country=models.CharField(max_length=50)
    operational=models.BooleanField(default=True)


class Driver(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    service_years=models.IntegerField(default=0)

    def increment_service_years(self):
        self.service_years+=1
        self.save()

#receivers
def post_driver_created_signal(sender, instance, **kwargs):
    print('After')
    print(instance)


def pre_driver_created_signal(sender, instance, **kwargs):
    print('Before')
    print(instance)


#trigger signals
post_save.connect(receiver=post_driver_created_signal, sender=Driver)

pre_save.connect(receiver=pre_driver_created_signal, sender=Driver)



