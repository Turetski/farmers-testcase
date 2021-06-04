from django.contrib import admin
from .models import *


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
