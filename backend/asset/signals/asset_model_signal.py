from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from asset.models.asset_model import AssetModel, AssetPriceModel
from asset.models import ActivePublicAssetingModel, AssetOwnershipModel


def calculate_changing_rate(old_price: float, new_price: float) -> float | int | None:
    if old_price != new_price:
        price_difference: float = new_price - old_price
        percentage_change: float = (price_difference / abs(old_price)) * 100
        if abs(percentage_change) >= 1:
            return round(percentage_change, 2)


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
    if created:
        asset_title: str = instance.name.replace(instance.code, '').strip()
        if active_offer := ActivePublicAssetingModel.objects.filter(title_eq=asset_title).first():
            print('halka arz tamamlandı')
            print(active_offer)


@receiver(pre_save, sender=AssetModel)
def profit_and_loss_calculator(sender, instance, **kwargs):
    if previous_instance := AssetModel.objects.filter(pk=instance.pk).first():
        old_price = previous_instance.current_price
        new_price = instance.current_price
        if change_rate := calculate_changing_rate(old_price, new_price):
            for asset_owner in AssetOwnershipModel.objects.filter(asset=instance):
                print(asset_owner)
                print(asset_owner.get_general_status())
                print(f"""
                    owner
                    old_price = {old_price}
                    new_price = {new_price},
                    old profit => {asset_owner.get_general_status(old_price)}
                    new profit => {asset_owner.get_general_status(new_price)}
                    """)

