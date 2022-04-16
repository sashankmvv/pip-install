from django.urls import path
from . import views


app_name="investor"
urlpatterns = [
    path('holding/<str:investor_id>/',
         views.get_holding, name='portfolio-holdings'),
#     path('listing/',
#          views.get_listing, name='portfolio-listings'),
     
]