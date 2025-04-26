from django.shortcuts import render
from .models import Currency, CurrencyName
import requests
import xmltodict
from django.utils import timezone
from datetime import datetime

def index(request):
    currency_objects = Currency.objects.all().order_by('-date')
    filtered_data = []

    code_query = request.GET.get('codes', '').replace(" ", "").upper()
    code_list = code_query.split(',') if code_query else []

    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')

    update = None

    if day and month and year:
        try:
            # ÖRNEK URL !!!!! 03 Şubat 2005 → https://www.tcmb.gov.tr/kurlar/200502/03022005.xml !!!!!
            tarih = f"{day.zfill(2)}{month.zfill(2)}{year}"
            url = f"https://www.tcmb.gov.tr/kurlar/{year}{month.zfill(2)}/{tarih}.xml"
            print(url)
            r = requests.get(url)

            if r.status_code != 200:
                update = None
                context = {
                    "Currency": [],
                    "update": None,
                    "error": "Seçilen tarihte TCMB kuru yayımlamamış olabilir. Lütfen hafta içi bir tarih seçiniz."
                }
                return render(request, "kur/index.html", context)

            data = xmltodict.parse(r.content)

            currencies = data["Tarih_Date"]["Currency"]
            update = data["Tarih_Date"]["@Date"]

            for item in currencies:
                kod = item["@Kod"]
                if not code_list or kod in code_list:
                    filtered_data.append({
                        "code": kod,
                        "buy": item.get("ForexBuying", "Yok"),
                        "sell": item.get("ForexSelling", "Yok"),
                        "date": update,
                    })

        except Exception as e:
            print("Hata:", e)

    context = {
        "Currency": filtered_data if (day and month and year) else currency_objects, "update": update,
    }

    return render(request, "kur/index.html", context)


'''
from django.shortcuts import render
from .models import Currency, CurrencyName

def index(request):
    currency_qs = Currency.objects.all().select_related('code')

    codes = request.GET.get("codes")
    date = request.GET.get("date")

    if codes:
        code_list = [code.strip().upper() for code in codes.split(',')]
        currency_qs = currency_qs.filter(code__name__in=code_list)

    if date:
        currency_qs = currency_qs.filter(date=date)

    context = {
        "Currency": currency_qs.order_by('-date'),
        "request": request,
    }
    return render(request, "kur/index.html", context)
'''

'''
from django.shortcuts import render
from .models import Currency

# Create your views here.

def index(request):
    currencies = Currency.objects.all()
    return render(request, 'kur/index.html', {'Currency': currencies, 'update': currencies.last().date})
'''