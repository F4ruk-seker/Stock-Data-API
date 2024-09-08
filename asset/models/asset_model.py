from django.db import models
from django.contrib.auth.models import User
from .utils import parse_price


class AssetPriceModel(models.Model):
    asset = models.ForeignKey('asset.AssetModel', on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class AssetModel(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(primary_key=True, unique=True, max_length=10)

    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    max_price = models.DecimalField(max_digits=20, decimal_places=2)
    min_price = models.DecimalField(max_digits=20, decimal_places=2)
    # price_flow = models.ManyToManyField('AssetPriceModel', blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    logo = models.URLField(default='', blank=True, null=True)
    url = models.URLField(default='', blank=True, null=True)
    chart = models.URLField(default='', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    updated_by = models.ForeignKey(User, null=True, default=None, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk is not None and self.current_price is not None:
            previous = AssetModel.objects.get(pk=self.pk)
            super().save(*args, **kwargs)
            if not previous.current_price == self.current_price:
                AssetPriceModel.objects.create(current_price=self.current_price, asset=self)
        else:
            super().save(*args, **kwargs)
            if self.current_price is not None:
                AssetPriceModel.objects.create(current_price=self.current_price, asset=self)
        super().save(*args, **kwargs)

    def get_price_flow(self):
        return self.AssetPriceModel.filter(asset=self).order_by('created_at')


