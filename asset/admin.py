from django.contrib import admin
from .models import *
from .models.asset_model import AssetPriceModel
from unfold.contrib.import_export.forms import ExportForm
from unfold.admin import ModelAdmin

admin.site.register(AssetPriceModel, ModelAdmin)
admin.site.register(ActivePublicAssetingModel, ModelAdmin)
admin.site.register(AssetOwnershipModel, ModelAdmin)
admin.site.register(SlotModel, ModelAdmin)
admin.site.register(FavoriteAssetModel, ModelAdmin)


@admin.register(AssetModel)
class ProductAdmin(ModelAdmin):
    list_display: tuple = 'code', 'current_price', 'percentage', 'image_tag', 'chart_tag'
    list_filter: tuple = 'updated_at',
    search_fields: tuple = 'name', 'code'
    readonly_fields: tuple = 'image_tag', 'chart_tag'
