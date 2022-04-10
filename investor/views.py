import operator
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from investor.models import BuyNSell, Investor
from property.models import Property
from user.models import Profile

# Create your views here.


def get_holding(request, investor_id):
    investor = Profile.objects.filter(aadhar_number=investor_id).first()
    investor = Investor.objects.filter(investor=investor)
    owner = Profile.objects.filter(aadhar_number=investor_id)
    property_list = Property.objects.filter(owner=owner)
    print(investor)
    for inv in investor:
        print(inv.current_price)
    profit_loss = [inv.current_price-inv.purchase_price for inv in investor]
    print(profit_loss)

    investor3 = Profile.objects.filter(aadhar_number=investor_id).first()
    print(investor3.aadhar_number)


    context = {
        'request':investor3,
       'investor':zip(investor,profit_loss),
       'investor_listing': property_list
    }

    # return render(request, 'investor/holding.html', context)
    return render(request, 'investor/investments.html', context)


# def get_listing(request, investor_id):
#     owner = Profile.objects.filter(aadhar_number=investor_id)
#     property = Property.objects.filter(owner=owner)

#     context = {
#         'investor_listing':property

#     }

#     print(context)
#     # return render(request, 'investor/holding.html', context)
#     return  render(request, 'investor/investments.html', context)

def buy(request,username,property):
    property = Property.objects.filter(propertyid=property).first()
    if request.method == 'POST':
        if request.POST.get('price'):
            post=BuyNSell()
            post.user=username
            post.property=property.propertyid
            post.price=request.POST.get('price')
            post.status=True
            post.save()
            context = {
                    'buyprop' : post,
                }
            return render(request, 'property/invest.html', context)  

def sell(request,username,property):
    property = Property.objects.filter(propertyid=property).first()
    if request.method == 'POST':
        if request.POST.get('price'):
            post=BuyNSell()
            post.user=username
            post.property=property.propertyid
            post.price=request.POST.get('price')
            post.status=False
            post.save()
            context = {
                    'sellprop' : post,
                }
            return render(request, 'property/invest.html', context)  



