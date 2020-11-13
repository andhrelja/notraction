from django.contrib import admin
from .models import (
    Championship,
    CategoryDriverPosition,
    Category,
    SubCategory
)

# Register your models here.
admin.site.register(Championship)
admin.site.register(CategoryDriverPosition)
admin.site.register(Category)
admin.site.register(SubCategory)
