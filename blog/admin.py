from django.contrib import admin
from hvad.admin import TranslatableAdmin
from models import Category, Post


class CategoryAdmin(TranslatableAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


class PostAdmin(TranslatableAdmin):
    pass

admin.site.register(Post, PostAdmin)