from django.contrib import admin
from .models import *

# Register your models here.

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('heroname', 'herolv')


class SkillsInfoAdmin(admin.ModelAdmin):
    list_display = ('skill', 'atk')



admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(SkillsInfo, SkillsInfoAdmin)
