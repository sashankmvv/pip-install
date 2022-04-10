from django.urls import path
from . import views

urlpatterns = [
    path('holding/<str:investor_id>/',
         views.get_holding, name='portfolio-holdings'),
    path('listing/<str:investor_id>/',
         views.get_listing, name='portfolio-listings'),
    

]
