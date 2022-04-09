from django.shortcuts import render
from property.models import Property
import ast

def home(request):
     return render(request,'property/home.html')

def invest(request):
     labels=[]
     data=[]
     queryset=Property.objects.all()
     print("queryset",queryset[0])
     # for investor in queryset:
     #      labels.append(investor.date)
     #      data.append(investor.purchase_price)
     
     for x in queryset:
          ps=  ast.literal_eval(x.price_series)
          ds=  ast.literal_eval(x.date_series)
          
          for i in range(len(ps)):
               data.append(ps[i])
               labels.append(ds[i])
     return render(request,'property/invest.html',{
          'labels':labels,
          'data':data,
     })
