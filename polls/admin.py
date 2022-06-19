from django.contrib import admin
from polls.models import *
# Register your models here.
class StyleInline(admin.TabularInline):
    model = Style
    extra = 5

class GenderAdmin(admin.ModelAdmin):
    inlines = [StyleInline]

class StylewebsiteInline(admin.TabularInline):
    model = StyleWebsite
    extra = 5

class StyleAdmin(admin.ModelAdmin):
    inlines = [StylewebsiteInline]


admin.site.register(Gender, GenderAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(StyleWebsite)
