from django.contrib import admin

# Register your models here.
from .models import Libro
class LibroAdmin(admin.ModelAdmin):
    radonly_fields = ("created_at", "updated_at")
    admin.site.register(Libro)