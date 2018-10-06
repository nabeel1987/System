from django.contrib import admin
from .models import Type
from .models import Items

from .models import Brand
from .models import ItemDetail
from .models import Category,Items
from import_export.admin import ImportExportModelAdmin

# Define the admin class

class CategoryAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Category, CategoryAdmin)


class TypeAdmin(admin.ModelAdmin):


    pass

# Register the admin class with the associated model
admin.site.register(Type, TypeAdmin)

class BrandAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Brand, BrandAdmin)

class ItemInstanceInline(admin.TabularInline):
    model = ItemDetail
    extra = 0

    list_display=('name','color',)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','brand','display_type','Quantity','Cost','SellPrice','status',)

    list_filter=('category_name','type_name','brand',)
    fieldsets = (
        ('Details', {
            'fields': ('name', 'brand', 'Quantity','Cost','SellPrice',)
        }),
        ('Sorting', {
            'fields': ('category_name', 'type_name',)
        }),
        ('Availability', {
            'fields': ('status', 'summary',)
        }),
    )

    inlines=[ItemInstanceInline]
    pass



# Register the admin class with the associated model
admin.site.register(Items, ItemAdmin)

class ItemDetailAdmin(admin.ModelAdmin):
    list_display=('item','color','condition')

    pass

# Register the admin class with the associated model
admin.site.register(ItemDetail, ItemDetailAdmin)
