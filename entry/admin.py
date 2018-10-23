from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from .models import *

# Register your models here.

class IncomeResource(ModelResource):
    class Meta:
        model = Income
    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''

class OutcomeResource(ModelResource):
    class Meta:
        model = Outcome
    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''

class TransferResource(ModelResource):
    class Meta:
        model = Transfer
    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''

@admin.register(Income)
class IncomeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']
    resource_class = IncomeResource

@admin.register(Outcome)
class OutcomeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']
    resource_class = OutcomeResource

@admin.register(Transfer)
class TransferAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']
    resource_class = TransferResource