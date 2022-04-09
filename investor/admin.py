from django.contrib import admin
from investor.models import Investor

from .models import Investor
# Register your models here.
admin.site.register(Investor)
