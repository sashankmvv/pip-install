from datetime import datetime
from operator import itemgetter
from django.shortcuts import render
from property.models import Property,Photos
import random
from investor.models import BuyNSell, Investor
from property.models import Property
import ast
import operator


def home(request):
     # properties=Property.objects.all()
     warehouse_items = list(Property.objects.filter(category='warehouse'))
     warehouse_random_items = random.sample(warehouse_items, 3)
     wpids = [warehouse_random_items[i].propertyid for i in range(3)]
     photos = [list(Photos.objects.filter(property=wpid))[0] for wpid in wpids]  
     # print(photos)
     # for x in photos:
     #      print(list(x)[0].photo)
     # office_items = list(Property.objects.filter(category='office-properties'))
     # office_random_items = random.sample(office_items, 3)
     # residential_items = list(Property.objects.filter(category='Residential-apartment'))
     # residential_random_items = random.sample(residential_items, 3)
     # context = {'warehouse_random_items': warehouse_random_items, 'office_items': office_items, 'residential_items': residential_items}
     context = {'warehouse_random_items': zip(warehouse_random_items, photos)}
     

     return render(request,'property/home.html',context)


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
    

    for buyer in sorted_buyers:
        for seller in sorted_sellers:
            if buyer.price == seller.price:
                if seller.quantity >= buyer.quantity:
                    seller.quantity = seller.quantity - buyer.quantity
                    buyer.quantity = 0
                    investor = Investor()
                    investor.property = property
                    investor.date = datetime.date()
                    investor.purchase_price = buyer.price
                    investor.rent_received = [0]
                    investor.status = True
                    investor.ownership_till = datetime.now()
                    buyer.delete()
                    break
                elif seller.quantity < buyer.quantity:
                    buyer.quantity = buyer.quantity - seller.quantity
                    investor = Investor.objects.filter(investor=seller).first()
                    investor.status = False
                    seller.quantity = 0
                    seller.delete()
                    break

    return render(request, 'property/invest.html', context)    


def allprop(request, ctgr):
    prop = Property.objects.filter(category=ctgr)
    context = {'prop': prop, }
    return render(request, 'property/all_properties.html', context)

