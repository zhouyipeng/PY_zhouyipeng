from django.contrib import admin
from .models import *

# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    # 显示字段，可以点击列头进行排序
    list_display = ('titie', 'pub_date')
    list_filter = ['titie']

    # inlines = [HeroInfoAdmin]

    def __str__(self):
        return 'titie'

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
