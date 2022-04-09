from django.db import models
from property.models import Property
from user.models import Profile
import json

# Create your models here.


class Investor(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, blank=False)
    investor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=False)
    date = models.DateField()
    purchase_price = models.DecimalField(
        decimal_places=2, max_digits=12, blank=False)
    ownership_till = models.DateField(null=True, blank=True)
    rent_received = models.DecimalField(
        decimal_places=2, max_digits=9, blank=False)
    # true = current owner of the property, false = past owner
    status = models.BooleanField(default=True)

    def setRent(self, x):
        self.rent_received = json.dumps(x)

    def getRent(self):
        return json.loads(self.rent_received)

    def __str__(self):
        return self.investor.userAuth.username