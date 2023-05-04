from django.contrib import admin
from .models import Region, District, Category, Product, ProductInfo, Comment, Message
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass

admin.site.register((
    Region,
    District,
    Category,
    ProductInfo,
    Comment,
    Message
))