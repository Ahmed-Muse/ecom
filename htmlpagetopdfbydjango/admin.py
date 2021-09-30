from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Customerpdf)
admin.site.register(Postpdf)
admin.site.register(Logopdf)

