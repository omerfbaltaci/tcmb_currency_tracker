import requests
import xmltodict
from .models import Currency
from .models import CurrencyName
from django.utils import timezone

def fetch_data():
    url = f"https://www.tcmb.gov.tr/kurlar/today.xml"
    d = requests.get(url)
    c = d.content
    data = xmltodict.parse(c)

    uptodate = data.get("Tarih_Date")

    json_list = data.get("Tarih_Date")
    currency_list = json_list.get("Currency")

    for i in currency_list:
        name_list = i.get("@Kod")
        buy_list = i.get("ForexBuying")
        sell_list = i.get("ForexSelling")

        if buy_list and sell_list:
            name_obj, _ = CurrencyName.objects.get_or_create(
                name = name_list,
            )
    
            Currency.objects.create(
                code = name_obj,
                buy = buy_list,
                sell = sell_list,
                date = timezone.now()
            )

