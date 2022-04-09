from django.urls import path
from . import views
urlpatterns = [
path('home/', views.home, name = 'Home'),
# path('invest/',views.invest,name='Invest'),
path('',views.invest,name='Invest'),
]