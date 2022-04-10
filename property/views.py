from django.shortcuts import render
from property.models import Property,Photos
import random
import ast

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

def invest(request,property):
     labels=[]
     data=[]
     queryset=Property.objects.filter(propertyid=property).first()
     
     # for investor in queryset:
     #      labels.append(investor.date)
     #      data.append(investor.purchase_price)
     

     ps = ast.literal_eval(queryset.price_series)
     ds = ast.literal_eval(queryset.date_series)

     for i in range(len(ps)):
          data.append(ps[i])
          labels.append(ds[i])
     return render(request, 'property/invest.html', {
          'labels': labels,
          'data': data,
          })


def allprop(request, ctgr):
    prop = Property.objects.filter(category=ctgr)
    context = {'prop': prop, }
    return render(request, 'property/all_properties.html', context)

