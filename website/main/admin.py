from django.contrib import admin
from .models import *
from django_admin_geomap import ModelAdmin
from .models import Location

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Location, ModelAdmin)

#все таблички регаем здесь
