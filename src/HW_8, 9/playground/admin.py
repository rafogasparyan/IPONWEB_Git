from django.contrib import admin
from .models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBag, Purchase


class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'registered_at', 'avatar']


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'registered_at', 'avatar']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_category', 'name', 'owner']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'category', 'price', 'quantity', 'description', 'store']


class ItemInline(admin.TabularInline):
    model = MyBag.items.through


class MyBagAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']
    inlines = [
        ItemInline,
    ]


class PurchaseInLine(admin.TabularInline):
    model = Purchase.items.through


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['buy_time', 'customer', 'total_price']
    inlines = [
        PurchaseInLine,
    ]


admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(MyBag, MyBagAdmin)
admin.site.register(Purchase, PurchaseAdmin)
