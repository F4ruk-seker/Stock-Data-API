from django.contrib import admin
from .models import *
from .models.asset_model import AssetPriceModel

admin.site.register(AssetModel)
admin.site.register(AssetPriceModel)
admin.site.register(ActivePublicAssetingModel)
admin.site.register(AssetOwnershipModel)
admin.site.register(SlotModel)
admin.site.register(FavoriteAssetModel)
