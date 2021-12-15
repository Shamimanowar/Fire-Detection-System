from django.contrib import admin
from .models import FireDetector


class DisplayValues(admin.ModelAdmin):
    list_display = [f.name for f in FireDetector._meta.fields]

# Register your models here.


admin.site.register(FireDetector, DisplayValues)
