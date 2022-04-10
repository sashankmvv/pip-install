from datetime import datetime
from operator import itemgetter
from user.models import Profile
from django.shortcuts import render
from investor.models import BuyNSell, Investor
from property.models import Property
import ast
import operator


def home(request):
    return render(request, 'property/home.html')


def invest(request,propertyid):
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
    user=request.user
    context = {
                    'property':property,
                    'labels' : labels,
                    'data': data,
                    'user':user,
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
    
    if request.method == 'POST':
        buy(request,property)

    return render(request, 'property/invest.html', context)


def allprop(request, ctgr):
    prop = Property.objects.filter(category=ctgr)
    context = {'prop': prop, }
    return render(request, 'property/all_properties.html', context)

def buy(request,property):
    # property2 = Property.objects.filter(propertyid=property).first()
    user=request.user
    user = Profile.objects.filter(userAuth=user).first()
    
    
    if request.method == 'POST':
        if request.POST.get('price') and request.POST.get('quantity'):
            post=BuyNSell()
            post.user=user
            post.property=property
            post.quantity=request.POST.get('quantity')
            post.price=request.POST.get('price')
            post.status=True
            post.save()
            context = {
                    'buyprop' : post,
                }
            return render(request, 'property/invest.html', context)  
    return render(request, 'property/home.html')  


