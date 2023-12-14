from django.contrib import admin
from .models import GalleryModel
# Register your models here.

@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'date']