from operator import itemgetter
from django.shortcuts import render
from investor.models import BuyNSell
from property.models import Property
import ast
import operator


def home(request):
    return render(request, 'property/home.html')


def invest(request, username,propertyid):
    labels = []
    data = []
    queryset = Property.objects.filter(propertyid=propertyid).first()

    # for investor in queryset:
    #      labels.append(investor.date)
    #      data.append(investor.purchase_price)

    ps = ast.literal_eval(queryset.price_series)
    ds = ast.literal_eval(queryset.date_series)

    for i in range(len(ps)):
        data.append(ps[i])
        labels.append(ds[i])

    property = Property.objects.filter(propertyid=propertyid).first()
    buy_n_sellers = BuyNSell.objects.filter(property=property)
    buyers = list(buy_n_sellers.filter(status=True))  # buyers
    sellers = list(buy_n_sellers.filter(status=False))  # sellers

    sorted_buyers = sorted(buyers, key=lambda x: x.datetime)
    sorted_sellers = sorted(sellers, key=lambda x: x.datetime)
    context = {
                    'labels' : labels,
                    'data': data,
                }
    
    return render(request, 'property/invest.html', context)


def allprop(request, ctgr):
    prop = Property.objects.filter(category=ctgr)
    context = {'prop': prop, }
    return render(request, 'property/all_properties.html', context)
