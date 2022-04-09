from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name = 'Home'),
# path('invest/',views.invest,name='Invest'),
# path('',views.invest,name='Invest'),
path('allproperties/<str:ctgr>/', views.allprop, name='AllProp'),
path('invest/<str:property>', views.invest, name='Invest'),

]
