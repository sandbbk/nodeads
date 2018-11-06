from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Group, Element


class GroupAdmin(MPTTModelAdmin):

    mptt_indent_field = "name"
    mptt_level_indent = 20
    list_display = ('name', 'icon_src', 'description', 'parent')
    list_display_links = ('name', 'parent')


class ElementAdmin(admin.ModelAdmin):
    fields = ['name', 'group', 'icon', 'is_modered', 'created_date', 'description']
    list_display = ('name', 'icon_src', 'description', 'group','is_modered', 'created_date')


admin.site.register(Group, GroupAdmin)
admin.site.register(Element, ElementAdmin)
