from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ForTestingOnly)
admin.site.register(Language)
admin.site.register(JsTest)
admin.site.register(DynamicFormThreeTable)
admin.site.register(QuotationTable)
admin.site.register(QuotationCustomerTable)


