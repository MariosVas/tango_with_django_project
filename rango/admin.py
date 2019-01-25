from django.contrib import admin
from rango.models import Category, Page




class PagesAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']}), (None, {'fields': ['category']}),
                 (None, {'fields': ['url']})]
    list_display = ("title", "category", "url")


admin.site.register(Category)
# admin.site.register(Page)
admin.site.register(Page, PagesAdmin)
# Register your models here.
