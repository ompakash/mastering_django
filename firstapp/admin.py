from django.contrib import admin
from firstapp.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductInCart)
admin.site.register(Order)