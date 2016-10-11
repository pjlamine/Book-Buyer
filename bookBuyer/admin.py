from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Cost

admin.site.register(Book)
admin.site.register(Cost)
