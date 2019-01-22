from django.db import models
import json
from django.core.serializers import serialize
from asset.models import *
from django.utils import timezone
import datetime
# Create your models here.

class Income(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    payed = models.BooleanField(default=False)
    account = models.ForeignKey('asset.Account', blank=False, null=None, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')+" - "+self.description+"("+str(self.amount)+")"

    
    def serialize(self):
        return json.dumps(json.loads(serialize('json', [self])))

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Incomes'
        db_table = 'incomes'

class Outcome(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey('asset.Category', blank=False, null=None, default=None, on_delete=models.CASCADE)
    account = models.ForeignKey('asset.Account', blank=False, null=None, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')+" - "+self.description+"("+str(self.amount)+")"

    
    def serialize(self):
        return json.dumps(json.loads(serialize('json', [self])))

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Outcomes'
        db_table = 'outcomes'

class Transfer(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    from_account = models.ForeignKey('asset.Account', blank=False, null=None, default=None, related_name="from_account", on_delete=models.CASCADE)
    to_account = models.ForeignKey('asset.Account', blank=False, null=None, default=None, related_name="to_account", on_delete=models.CASCADE)
    taxes = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')+" - "+self.description+"("+str(self.amount)+")"

    
    def serialize(self):
        return json.dumps(json.loads(serialize('json', [self])))
 
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Transfers'
        db_table = 'transfers'
