from django.contrib import admin

# Register your models here.

from .models import Category
from .models import Heritage
from .models import Location

admin.site.register(Category)
admin.site.register(Heritage)
admin.site.register(Location)