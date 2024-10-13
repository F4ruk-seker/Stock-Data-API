from django.db import models
from django.contrib.auth.models import User


class FavoriteAssetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey('asset.AssetModel', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
