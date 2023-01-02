from django.db import models

# Create your models here.

class country_codes(models.Model):
    domain = models.CharField(max_length=15)
    country = models.CharField(max_length=100,blank=True,null=True)
class wordlist(models.Model):
    word = models.CharField(max_length=100)
class wordlistmain(models.Model):
    name = models.CharField(max_length=100)
    wordlist = models.ManyToManyField(wordlist,blank=True)
class dorkcontents(models.Model):
    dork = models.CharField(max_length=200)
class dorktype(models.Model):
    name = models.CharField(max_length=100)
    dork = models.ManyToManyField(dorkcontents)
