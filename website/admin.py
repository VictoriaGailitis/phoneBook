from django.contrib import admin
from .models import Record
from import_export.admin import ImportExportModelAdmin

class recordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Record, recordAdmin)

