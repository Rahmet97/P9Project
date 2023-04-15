from django.contrib import admin
from .models import Region, District, Category, Product, ProductInfo, Comment

admin.site.register((Region, District, Category, Product, ProductInfo, Comment))