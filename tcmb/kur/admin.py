from django.contrib import admin
from .models import Currency, CurrencyName

# Register your models here.

admin.site.register(Currency)
admin.site.register(CurrencyName)
