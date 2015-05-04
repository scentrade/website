from django.contrib import admin
from hvad.admin import TranslatableAdmin
from store.models import Category, Product


class CategoryAdmin(TranslatableAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslatableAdmin):
    pass

admin.site.register(Product, ProductAdmin)