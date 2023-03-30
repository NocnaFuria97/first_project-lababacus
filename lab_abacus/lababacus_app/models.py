from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=64)

class Animal(models.Model):
    name_or_number = models.CharField(max_length=64)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

class Blood(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    no_neutro_seg = models.IntegerField()
    no_neutro_non_seg = models.IntegerField()
    no_bazo = models.IntegerField()
    no_eozyno = models.IntegerField()
    no_limfo = models.IntegerField()
    no_mono = models.IntegerField()
    no_trombo = models.IntegerField()
    added_date_blood = models.DateField(auto_now_add=True)

class Nosema(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    apis = models.IntegerField()
    cerane = models.IntegerField()
    added_date_nosema = models.DateField(auto_now_add=True)






