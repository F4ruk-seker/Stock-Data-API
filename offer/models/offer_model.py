from django.db import models
from django.contrib.auth.models import User


class OfferModel(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(primary_key=True, unique=True, max_length=10)

    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    max_price = models.DecimalField(max_digits=20, decimal_places=2)
    min_price = models.DecimalField(max_digits=20, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    logo = models.URLField(default='', blank=True, null=True)
    url = models.URLField(default='', blank=True, null=True)
    chart = models.URLField(default='', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    updated_by = models.ForeignKey(User, null=True, default=None, blank=True, on_delete=models.CASCADE)

