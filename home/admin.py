from django.contrib import admin
from .models import contact

# Register your models here.
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile_no')