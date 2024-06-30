from django.contrib import admin
from .models import Condition


class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'text')
    list_display_links = ('id', 'code', 'text')
    search_fields = ('id', 'code', 'text')


admin.site.register(Condition, ConditionAdmin)
