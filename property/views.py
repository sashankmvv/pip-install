from django.shortcuts import render
from property.models import Property
import ast

def home(request):
     return render(request,'property/home.html')

def invest(request,property):
     labels=[]
     data=[]
<<<<<<< HEAD
     queryset=Property.objects.all()
 
=======
     queryset=Property.objects.filter(propertyid=property).first()
     
>>>>>>> 7fc4b4a82c69424ba87d146c2d1ad66155cf9048
     # for investor in queryset:
     #      labels.append(investor.date)
     #      data.append(investor.purchase_price)
     
<<<<<<< HEAD

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
=======
     
     ps=  ast.literal_eval(queryset.price_series)
     ds=  ast.literal_eval(queryset.date_series)
          
     for i in range(len(ps)):
          data.append(ps[i])
          labels.append(ds[i])
     return render(request,'property/invest.html',{
          'labels':labels,
          'data':data,
     })
>>>>>>> 7fc4b4a82c69424ba87d146c2d1ad66155cf9048
