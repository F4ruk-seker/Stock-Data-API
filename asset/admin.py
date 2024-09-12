from django.contrib import admin
from .models import *
from .models.asset_model import AssetPriceModel

admin.site.register(AssetPriceModel)
admin.site.register(ActivePublicAssetingModel)
admin.site.register(AssetOwnershipModel)
admin.site.register(SlotModel)
admin.site.register(FavoriteAssetModel)


@admin.register(AssetModel)
class ProductAdmin(admin.ModelAdmin):
    list_display: tuple = 'code', 'current_price', 'percentage', 'image_tag', 'chart_tag'
    list_filter: tuple = 'updated_at',
    search_fields: tuple = 'name', 'code'
    readonly_fields: tuple = 'image_tag', 'chart_tag'
