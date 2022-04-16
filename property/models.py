from django.db import models
from django.core.validators import RegexValidator
from user.models import Profile
import json


def dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/photos/propertyid/<filename>
    return 'photos/{0}/{1}'.format(instance.property.propertyid, filename)

# Create your models here.


class Property(models.Model):
    property_name = models.CharField(max_length=100, default="")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    propertyid = models.CharField(max_length=10, primary_key=True)
    location = models.CharField(max_length=30, blank=False)
    address = models.TextField(blank=False)
    area_sqm = models.DecimalField(decimal_places=2, max_digits=9, blank=False)
    listing_price = models.DecimalField(
        decimal_places=2, max_digits=12, blank=False)
    current_price = models.DecimalField(
        decimal_places=2, max_digits=12, blank=False)
    market_price = models.DecimalField(
        decimal_places=2, max_digits=12, blank=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    tenant = models.CharField(max_length=30, blank=False)
    rent = models.DecimalField(decimal_places=2, max_digits=7, blank=False)
    contact = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    lock_in_period = models.DecimalField(
        decimal_places=2, max_digits=5, blank=False)
    lease_period = models.DecimalField(
        decimal_places=2, max_digits=5, blank=False)
    dilution = models.DecimalField(decimal_places=2, max_digits=4, blank=False)
    # 0 for not approved, 1 for approved
    approval_status = models.IntegerField(default=0)

    price_series = models.CharField(max_length=1000, blank=True)
    date_series = models.CharField(max_length=1000, blank=True)
    CATEGORY = (('warehouse', 'warehouse'),
                ('office-properties', 'office-properties'),
                ('Residential-apartment', 'Residential apartment'))

    category = models.CharField(max_length=50, choices=CATEGORY, default='')

    def assignPrices(self, x):
        """assigns list of prices for current property as a string

        Args:
            x (list): list of prices for current property
        """
        self.price_series = json.dumps(x)

    def getPrices(self):
        """returns list of prices for current property

        Returns:
            list: list of prices for current property
        """
        return json.loads(self.price_series)

    def assignDates(self, x):
        """assigns list of dates w.r.t price for current property as a string

        Args:
            x (list): list of dates for current property
        """
        self.date_series = json.dumps(x)

    def getDates(self):
        """assigns list of dates w.r.t price for current property as a string

        Returns:
            list: list of dates for current property
        """
        return json.loads(self.date_series)

    def __str__(self):
        return self.property_name


class Photos(models.Model):
    photo = models.FileField(upload_to=dir_path)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='properties')
