from django.contrib import admin
from .models import *
    
admin.site.register(StoreCategory)
admin.site.register(Store)
admin.site.register(ProductPrice)
admin.site.register(ProductOffer)