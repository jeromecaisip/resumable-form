from django.db import models
from easy_loan.users.models import Profile


# Create your models here.
class Employment(models.Model):
    profile = models.ForeignKey(Profile, related_name='employment_history', on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Guarantor(models.Model):
    profile = models.ForeignKey(Profile, related_name='guarantors', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
