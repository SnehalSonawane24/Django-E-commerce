from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ecommerce.models import User, Product, Order


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'retailer')
    search_fields = ('name',)
    list_filter = ('retailer',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'get_products', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username', 'customer__email')

    def get_products(self, obj):
        return ", ".join([p.name for p in obj.products.all()])
    get_products.short_description = 'Products'


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)