from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CustomerTable)
admin.site.register(ProductTable)
admin.site.register(OrderTable)
admin.site.register(OrderItemTable)
admin.site.register(ShippingAddressTable)
