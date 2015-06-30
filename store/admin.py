from adminsortable.admin import SortableAdmin
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from store.models import Category, Product, Buyer, Purchase


class CategoryAdmin(TranslatableAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslatableAdmin, SortableAdmin):
    pass

admin.site.register(Product, ProductAdmin)

admin.site.register(Buyer)
admin.site.register(Purchase)