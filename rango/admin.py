from django.contrib import admin
from rango.models import Category, Page
from .models import MyModel

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(MyModel)