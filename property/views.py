from django.shortcuts import render
from property.models import Property

def home(request):
     return render(request,'property/home.html')

def invest(request):
     labels=[]
     data=[]
     print("abc")
     queryset=Property.objects.all()
     # for investor in queryset:
     #      labels.append(investor.date)
     #      data.append(investor.purchase_price)
     return render(request,'property/invest.html',{
          'labels':labels,
          'data':data,
     })
