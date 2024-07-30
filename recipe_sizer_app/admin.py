from django.contrib import admin

# Register your models here.
from .models import MeasureType, Measure, Recipe

#admin.site.register(MeasureChoices)  only import and register classes ... update with relational model implemented ... 
admin.site.register(MeasureType)
admin.site.register(Measure)
admin.site.register(Recipe)