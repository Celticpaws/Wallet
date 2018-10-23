from django.db import models
import json
from django.core.serializers import serialize
# Create your models here.

class Account(models.Model):
    id = models.CharField(max_length=3, primary_key=True, default='XXX')
    number = models.CharField(max_length=40, unique = True, blank = False, null = False, default=0)
    bank = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.bank+" - ("+self.id+")"

    
    def serialize(self):
        return json.dumps(json.loads(serialize('json', [self])))

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Accounts'
        db_table = 'accounts'


class Category(models.Model):
    id = models.CharField(max_length=3, primary_key=True, default='XXX')
    name = models.CharField(max_length=100, blank=True, null=True)
    father = models.ForeignKey('Category', blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.id+" - "+self.name

    
    def serialize(self):
        return json.dumps(json.loads(serialize('json', [self])))

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Categories'
        db_table = 'categories'

