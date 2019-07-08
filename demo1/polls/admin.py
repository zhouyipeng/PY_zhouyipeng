from django.contrib import admin
from .models import *

# Register your models here.

class PollsInfoAdmin(admin.ModelAdmin):
    list_display = ('vote', 'votetime')


    def __str__(self):
        return self.fields

class VoteInfoAdmin(admin.ModelAdmin):
    list_display = ('category','poll')

    def __str__(self):
        return self.list_display, self.fields

admin.site.register(PollsInfo, PollsInfoAdmin)
admin.site.register(VoteInfo, VoteInfoAdmin)
