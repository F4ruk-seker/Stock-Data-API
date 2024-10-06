from django.db import models


class ActivePublicAssetingModel(models.Model):
    # Title of the company
    title = models.CharField(max_length=255)

    # URL for more details
    url = models.URLField(max_length=500)

    # Sale price of the stock
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Date range for collecting requests
    request_start_date = models.DateField()
    request_end_date = models.DateField()

    # Number of lots to be sold
    lots_to_be_sold = models.BigIntegerField()

    # Total IPO size
    ipo_size = models.DecimalField(max_digits=15, decimal_places=2)

    # Distribution method (e.g., Equal to individual investors)
    distribution_method = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.title
