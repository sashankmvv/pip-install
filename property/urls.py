from django.urls import path
from . import views
urlpatterns = [
    path('invest/', views.home, name='Home'),
    path('allproperties/<str:ctgr>/', views.allprop, name='AllProp'),
    path('invest/<str:username>/<str:propertyid>', views.invest, name='Invest'),

]
