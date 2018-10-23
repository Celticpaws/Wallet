from django.db import models
from asset.models import *

import datetime
# Create your models here.
class Budget(models.Model):
    date = models.DateField(default=datetime.datetime.now())
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('asset.Category', blank=False, null=None, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime('%Y-%m')+" - "+self.category.id+"("+str(self.amount)+")"

    
    def serialize(self):
        return json.dumps(json.loads(serialize('json', [self])))

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Budgets'
        db_table = 'budgets'