from django.contrib import admin

# Register your models here.
from app01.models import Book


class BookConfig(admin.ModelAdmin):
    pass

admin.site.register(Book)