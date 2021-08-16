from django.contrib import admin

# Register your models here.

from .models import Provider, Polygon

admin.site.register(Provider)
admin.site.register(Polygon)
