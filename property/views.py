import datetime
from operator import itemgetter
from user.models import Profile
from django.shortcuts import redirect, render
from property.models import Property, Photos
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

    return render(request, 'property/home.html', context)


def invest(request, propertyid):
<<<<<<< HEAD
=======
    print("abc")
>>>>>>> 6eaed036d6504abdbd7df88a6c91142db34b5f5d
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

    user = request.user
    context = {
        'property': property,
        'labels': labels,
        'data': data,
        'user': user,
    }

#     property = Property.objects.filter(propertyid=propertyid).first()
#     print(property)
#     buy_n_sellers = BuyNSell.objects.filter(property=property)
#     buyers = list(buy_n_sellers.filter(status=True))  # buyers
#     sellers = list(buy_n_sellers.filter(status=False))  # sellers

#     sorted_buyers = sorted(buyers, key=lambda x: x.datetime)
#     sorted_sellers = sorted(sellers, key=lambda x: x.datetime)

#     print(sorted_buyers, sorted_sellers)

#     print("Inside match logic : ")

#     for buyer in sorted_buyers:
#         for seller in sorted_sellers:
#             print(buyer.price, seller.price)
#             if buyer.price == seller.price:
#                 if seller.quantity > buyer.quantity:
#                     seller.quantity = seller.quantity - buyer.quantity
#                     investor = Investor()
#                     investor.property = property
#                     investor.investor = buyer.user
#                     investor.date = datetime.date.today()
#                     investor.purchase_price = buyer.price
#                     investor.rent_received = 0
#                     investor.status = True
#                     investor.ownership_till = datetime.datetime.now()
#                     investor.save()

#                     property.current_price = buyer.price
#                     prices = property.getPrices()
#                     prices.append(float(buyer.price))
#                     print(prices)
#                     property.assignPrices(prices)

#                     dates = property.getPrices()
#                     dates.append(str(datetime.datetime.now()))
#                     print(dates)
#                     property.assignDates(dates)
#                     property.save()

#                     buyer.delete()
#                     break
#                 elif seller.quantity < buyer.quantity:
#                     buyer.quantity = buyer.quantity - seller.quantity
#                     investor = Investor.objects.filter(
#                         investor=seller.user).first()
#                     investor.status = False
#                     investor.save()

#                     seller.quantity = 0

#                     property.current_price = buyer.price
#                     prices = property.getPrices()
#                     prices.append(float(buyer.price))
#                     property.assignPrices(prices)

#                     dates = property.getPrices()
#                     dates.append(str(datetime.datetime.now()))
#                     property.assignDates(dates)
#                     property.save()

#                     seller.delete()
#                     break
#                 elif seller.quantity == buyer.quantity:
#                     seller.quantity = seller.quantity - buyer.quantity
#                     buyer.quantity += seller.quantity

#                     investor = Investor.objects.filter(
#                         investor=seller.user).first()
#                     print(investor)

#                     investor.status = False
#                     investor.save()
#                     seller.quantity = 0

#                     investor = Investor()
#                     investor.property = property
#                     investor.investor = buyer.user
#                     investor.date = datetime.date.today()
#                     investor.purchase_price = buyer.price
#                     investor.rent_received = 0
#                     investor.status = True
#                     investor.ownership_till = datetime.datetime.now()
#                     investor.save()

#                     property.current_price = buyer.price
#                     prices = property.getPrices()
#                     prices.append(float(buyer.price))
#                     print(prices)
#                     property.assignPrices(prices)

#                     dates = property.getPrices()
#                     dates.append(str(datetime.datetime.now()))
#                     print(dates)
#                     property.assignDates(dates)
#                     print(property.current_price)
#                     property.save()

#                     print(buyer)
#                     buyer.delete()
#                     print(seller)
#                     seller.delete()
#                     break

    if request.method == 'POST':
        buy(request, property)

    return render(request, 'property/invest.html', context)


def allprop(request, ctgr):
    prop = Property.objects.filter(category=ctgr)
    context = {'prop': prop, }
    return render(request, 'property/all_properties.html', context)


def buy(request, property):
    # property2 = Property.objects.filter(propertyid=property).first()
    user = request.user
    user = Profile.objects.filter(userAuth=user).first()

    if request.method == 'POST':
        if request.POST.get('buyprice') and request.POST.get('buyquantity'):
            post = BuyNSell()
            post.user = user
            post.property = property
            post.quantity = request.POST.get('buyquantity')
            post.price = request.POST.get('buyprice')
            post.status = True
            post.save()
            context = {
                'buyprop': post,
            }
            match(request, property.propertyid)

            user = request.user
            user = Profile.objects.filter(userAuth=user).first()
            context = {
                'buyprop': post,
            }
            return render(request, 'property/invest.html', context)

        elif request.POST.get('sellprice') and request.POST.get('sellquantity'):
            post = BuyNSell()
            post.user = user
            post.property = property
            post.quantity = request.POST.get('sellquantity')
            post.price = request.POST.get('sellprice')
            post.status = False
            post.save()
            context = {
                'sellprop': post,
            }
            match(request, property.propertyid)

            return render(request, 'property/invest.html', context)


def match(request, propertyid):
    property = Property.objects.filter(propertyid=propertyid).first()
    print(property)
    buy_n_sellers = BuyNSell.objects.filter(property=property)
    buyers = list(buy_n_sellers.filter(status=True))  # buyers
    sellers = list(buy_n_sellers.filter(status=False))  # sellers

    sorted_buyers = sorted(buyers, key=lambda x: x.datetime)
    sorted_sellers = sorted(sellers, key=lambda x: x.datetime)

    print(sorted_buyers, sorted_sellers)

    print("Inside match logic : ")

    for buyer in sorted_buyers:
        for seller in sorted_sellers:
            print(buyer.price, seller.price)
            if buyer.price == seller.price:
                if seller.quantity > buyer.quantity:
                    seller.quantity = seller.quantity - buyer.quantity
                    investor = Investor()
                    investor.property = property
                    investor.investor = buyer.user
                    investor.date = datetime.date.today()
                    investor.purchase_price = buyer.price
                    investor.rent_received = 0
                    investor.status = True
                    investor.ownership_till = datetime.datetime.now()
                    investor.save()

                    property.current_price = buyer.price
                    prices = property.getPrices()
                    prices.append(float(buyer.price))
                    print(prices)
                    property.assignPrices(prices)

                    dates = property.getDates()
                    dates.append(str(datetime.datetime.now()))
                    print(dates)
                    property.assignDates(dates)
                    property.save()

                    buyer.delete()
                    break
                elif seller.quantity < buyer.quantity:
                    buyer.quantity = buyer.quantity - seller.quantity
                    investor = Investor.objects.filter(
                        investor=seller.user).first()
                    investor.status = False
                    investor.save()

                    seller.quantity = 0

                    property.current_price = buyer.price
                    prices = property.getPrices()
                    prices.append(float(buyer.price))
                    property.assignPrices(prices)

                    dates = property.getDates()
                    dates.append(str(datetime.datetime.now()))
                    property.assignDates(dates)
                    property.save()

                    seller.delete()
                    break
                elif seller.quantity == buyer.quantity:
                    seller.quantity = seller.quantity - buyer.quantity
                    buyer.quantity += seller.quantity

                    investor = Investor.objects.filter(
                        investor=seller.user).first()
                    print(investor)

                    investor.status = False
                    investor.save()
                    seller.quantity = 0

                    investor = Investor()
                    investor.property = property
                    investor.investor = buyer.user
                    investor.date = datetime.date.today()
                    investor.purchase_price = buyer.price
                    investor.rent_received = 0
                    investor.status = True
                    investor.ownership_till = datetime.datetime.now()
                    investor.save()

                    property.current_price = buyer.price
                    prices = property.getPrices()
                    prices.append(float(buyer.price))
                    print(prices)
                    property.assignPrices(prices)

                    dates = property.getDates()
                    dates.append(str(datetime.datetime.now()))
                    print(dates)
                    property.assignDates(dates)
                    print(property.current_price)
                    property.save()

                    print(buyer)
                    buyer.delete()
                    print(seller)
                    seller.delete()
                    break
