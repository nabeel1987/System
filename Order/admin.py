from django.contrib import admin
from .models import NewOrder
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=['OrderName','Customer','Inventory',]


admin.site.register(NewOrder,OrderAdmin)
