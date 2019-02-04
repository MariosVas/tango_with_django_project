from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PagesAdmin(admin.ModelAdmin):
    # fieldsets = [(None, {'fields': ['title']}), (None, {'fields': ['category']}),
    #              (None, {'fields': ['url']})]
    list_display = ("title", "category", "url")


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PagesAdmin)
# admin.site.register(Category)
# admin.site.register(Page)
# Register your models here.
