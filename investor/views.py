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
    print(investor)
    property_list=[Property.objects.filter(propertyid=x.property.propertyid).first() for x in investor]
    print("P",property_list)
    # owner = Profile.objects.filter(aadhar_number=investor_id).first()
    # property_list = Property.objects.filter(owner=owner)
    # print(property_list)
    # for inv,x in zip(investor,property_list):
    #     print(x.current_price)
    # print(type(inv.purchase_price))
    profit_loss = [int(x.current_price-inv.purchase_price) for inv,x in zip(investor,property_list)]
    
    investor3 = Profile.objects.filter(aadhar_number=investor_id).first()
    print(investor3.aadhar_number)
    print(profit_loss)
    print(property_list)
    context = {
        'request':investor3,
       'profit_prop_inv':zip(profit_loss,property_list,investor),
        
    #    'investor':zip(Investor.objects.filter(investor=inv1).last(),profit_loss)
      
    }
    
    # return render(request, 'investor/holding.html', context)
    return render(request, 'investor/investments.html', context)


# def get_listing(request):
#     # owner = Profile.objects.filter(aadhar_number=investor_id)
#     # property = Property.objects.filter(owner=owner)

#     # context = {
#     #     'investor_listing':property

#     # }

#     # print(context)
#     # # return render(request, 'investor/holding.html', context)
#     return  render(request, 'investor/investments.html')

# def buy(request,property):
#     property = Property.objects.filter(propertyid=property).first()
#     user=request.user
#     if request.method == 'POST':
#         if request.POST.get('price') and request.POST.get('quantity'):
#             post=BuyNSell()
#             post.user=user.username
#             post.property=property.propertyid
#             post.quantity=request.POST.get('quantity')
#             post.price=request.POST.get('price')
#             post.status=True
#             post.save()
#             context = {
#                     'buyprop' : post,
#                 }
#             return render(request, 'property/invest.html', context)  
#     return render(request, 'property/home.html')  

# def sell(request,username,property):
#     property = Property.objects.filter(propertyid=property).first()
#     if request.method == 'POST':
#         if request.POST.get('price') and request.POST.get('quantity'):
#             post=BuyNSell()
#             post.user=username
#             post.property=property.propertyid
#             post.quantity=request.POST.get('quantity')
#             post.price=request.POST.get('price')
#             post.status=False
#             post.save()
#             context = {
#                     'sellprop' : post,
#                 }
#             return render(request, 'property/invest.html', context)  



