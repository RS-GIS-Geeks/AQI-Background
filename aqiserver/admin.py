from django.contrib import admin
from aqiserver import models

# Register your models here.
admin.site.register(models.Aqidaydata)
admin.site.register(models.Aqimonthdata)
admin.site.register(models.City)
admin.site.register(models.Province)
