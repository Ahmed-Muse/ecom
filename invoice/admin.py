from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *

admin.site.register(ClientsModel)
admin.site.register(InvoicesModel)
admin.site.register(ProductsModel)
admin.site.register(SettingsModel)