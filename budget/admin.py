from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from .models import *

# Register your models here.
class BudgetResource(ModelResource):
    class Meta:
        model = Budget
    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''

@admin.register(Budget)
class BudgetAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date','category']
    resource_class = BudgetResource