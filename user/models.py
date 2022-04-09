from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/docs/email/<filename>
    return 'docs/{0}/{1}'.format(instance.email, filename)


class Profile(models.Model):
    # personal details
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    aadhar_number = models.IntegerField(primary_key=True)
    pan_number = models.IntegerField()
    dob = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    # bank details
    bank_name = models.CharField(max_length=50)
    bank_account_number = models.IntegerField()
    bank_IFSC_code = models.CharField(max_length=12)

    # documents
    aadhar_proof = models.FileField(upload_to=user_directory_path)
    pan_proof = models.FileField(upload_to=user_directory_path)
    bank_proof = models.FileField(upload_to=user_directory_path)

    # other details
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.aadhar_number)
