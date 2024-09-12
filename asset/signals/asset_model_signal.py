from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from asset.models.asset_model import AssetModel, AssetPriceModel


@receiver(pre_save, sender=AssetModel)
def pre_sync_asset_price_flow(sender, instance, **kwargs):
    if instance.pk:
        try:
            previous_instance = AssetModel.objects.get(pk=instance.pk)
            old_price = previous_instance.current_price
            new_price = instance.current_price

            if old_price != new_price:
                AssetPriceModel.objects.create(current_price=new_price, asset=instance)

        except AssetModel.DoesNotExist:
            pass  # known


@receiver(post_save, sender=AssetModel)
def sync_asset_price_flow(sender, instance, created, **kwargs):
    if created:
        AssetPriceModel.objects.create(current_price=instance.current_price, asset=instance)
