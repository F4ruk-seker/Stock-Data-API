from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from asset.models.asset_model import AssetModel, AssetPriceModel
from asset.models import ActivePublicAssetingModel, AssetOwnershipModel
from django.core.mail import send_mail
from asset.tasks import new_active_public_asset_alerts
from django.contrib.auth.models import User


@receiver(post_save, sender=AssetModel)
def create_new_active_public_asset_alert(sender, instance, created, **kwargs):
    if created:
        for user in User.objects.filter(email__isnull=False):
            # EXAMPLE
            new_active_public_asset_alerts.delay(
                user_email=user.email,
                context={
                    "code": 'PARS',
                },
                subject='Offer is ready'
            )
