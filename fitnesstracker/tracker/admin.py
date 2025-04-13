from django.contrib import admin

# Register your models here.

from .models import Activity, Workout  # 👈 import your models

admin.site.register(Activity)
admin.site.register(Workout)