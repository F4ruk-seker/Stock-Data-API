from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


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

    def image_tag(self):
        if image_src := self.logo:
            return mark_safe(f'<img src="{image_src}" width="30px" height="30px" style="object-fit:cover">')
        else:
            return mark_safe('<span style="color:red">None</span>')

    def chart_tag(self):
        if image_src := self.chart:
            return mark_safe(f'<img src="{image_src}" width="30px" height="30px" style="object-fit:cover">')
        else:
            return mark_safe('<span style="color:red">None</span>')

    image_tag.short_description = 'Image'

    chart_tag.short_description = 'Chart'

    def get_price_flow(self):
        return self.AssetPriceModel.filter(asset=self).order_by('created_at')


