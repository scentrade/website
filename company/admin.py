from django.contrib import admin
from hvad.admin import TranslatableAdmin
from models import Client, Testimony


admin.site.register(Client)


class TestimonyAdmin(TranslatableAdmin):
    pass

admin.site.register(Testimony, TestimonyAdmin)