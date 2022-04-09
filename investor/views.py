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
    investor = Investor.objects.filter(investor=investor).first()

    context = {
        'property_name': investor.property.property_name,
        'purchase_price': investor.purchase_price,
        'purchase_date': investor.date,
        'current_price': investor.property.current_price,
    }

    print(context)
    # return render(request, 'investor/holding.html', context)
    return HttpResponse(context)


def get_listing(request, investor_id):
    owner = Profile.objects.filter(aadhar_number=investor_id).first()
    property = Property.objects.filter(owner=owner).first()

    context = {
        'property_name': property.property_name,
        'listing_price': property.listing_price,
        'current_price': property.current_price,
        'market_price': property.market_price,
    }

    print(context)
    # return render(request, 'investor/holding.html', context)
    return HttpResponse(context)



