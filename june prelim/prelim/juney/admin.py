from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Consultation


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_submitted')
    search_fields = ('name', 'email')
    list_filter = ('date_submitted',)