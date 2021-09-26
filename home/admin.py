from django.contrib import admin

# Register your models here.
from . models import *
# Register your models here.
#name copy to slug
class catagadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(categor,catagadmin)
class prdadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','price','stock','available']
    list_editable = ['price','stock','available']
admin.site.register(product,prdadmin)