from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'type', 'category', 'date')
    list_filter = ('type', 'category', 'date')
    search_fields = ('category', 'notes')
    ordering = ('-date',)