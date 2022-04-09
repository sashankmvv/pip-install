from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name = 'Home'),
# path('invest/',views.invest,name='Invest'),
path('invest/<str:property>',views.invest,name='Invest'),
]