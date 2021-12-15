from django.contrib import admin
from django.db import models
from .models import FireDetector


class DisplayValues(admin.ModelAdmin):
    list_display = [f.name for f in FireDetector._meta.fields]

    class Meta:
        model = FireDetector

# Register your models here.


admin.site.register(FireDetector, DisplayValues)
