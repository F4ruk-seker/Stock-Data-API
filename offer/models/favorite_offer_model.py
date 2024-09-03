from django.db import models
from django.contrib.auth.models import User


class FavoriteOfferModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey('offer.OfferModel', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
