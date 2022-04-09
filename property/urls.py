from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name = 'Home'),
# path('invest/',views.invest,name='Invest'),
<<<<<<< HEAD
# path('',views.invest,name='Invest'),
path('allproperties/<str:ctgr>/', views.allprop, name='AllProp'),
path('invest/<str:property>', views.invest, name='Invest'),

]
=======
path('invest/<str:property>',views.invest,name='Invest'),
]
>>>>>>> 7fc4b4a82c69424ba87d146c2d1ad66155cf9048
