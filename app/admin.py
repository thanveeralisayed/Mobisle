from django.contrib import admin
from .models import Customer,Order,Product,Cart

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)