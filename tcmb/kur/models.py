from django.db import models

# Create your models here.

class CurrencyName(models.Model):
    name = models.CharField(max_length= 10, null=True, blank=True,)

    def __str__(self):
        return self.name

class Currency(models.Model):
    code = models.ForeignKey(CurrencyName, on_delete=models.CASCADE, null=True, blank=True,)
    buy = models.DecimalField(max_digits= 10, decimal_places= 4, null=True, blank=True,)
    sell = models.DecimalField(max_digits= 10, decimal_places= 4, null=True, blank=True,)
    date = models.DateField(auto_now_add= True, null=True, blank=True,)

    def __str__(self):
        return f"{self.code}"
