from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from .models import *

# Register your models here.
class AccountResource(ModelResource):
    class Meta:
        model = Account
    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''

class CategoryResource(ModelResource):
    class Meta:
        model = Category
    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''

@admin.register(Account)
class AccountAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AccountResource

@admin.register(Category)
class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['father']
    resource_class = CategoryResource