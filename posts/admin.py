from django.contrib import admin
from .models import Product, Review
# Register your models here.
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'view_count',
        'created_at',
    )
    list_filter=(
        'permission',
    )
    search_fields=(
        'id',
        'title'
    )



admin.site.register(Review)