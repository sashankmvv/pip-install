from django.db import models
from django.core.validators import RegexValidator


def dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/photos/propertyid/<filename>
    return 'photos/{0}/{1}'.format(instance.property.propertyid, filename)

# Create your models here.


class Property(models.Model):
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
    owner = models.CharField(max_length=30, blank=False)
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


class Photos(models.Model):
    photo = models.FileField(upload_to=dir_path)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='properties')