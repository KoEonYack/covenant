from django.contrib import admin
from sellbuy.models import SellPost
# Register your models here.


class SellAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']

admin.site.register(SellPost, SellAdmin)