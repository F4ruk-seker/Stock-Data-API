from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from asset.models.asset_model import AssetModel, AssetPriceModel
from asset.models import ActivePublicAssetingModel, AssetOwnershipModel
from django.core.mail import send_mail


@receiver(post_save, sender=AssetModel)
def create_new_active_public_asset_alert(sender, instance, created, **kwargs):

    send_mail(
        'Konu Başlığı',
        'Mesaj içeriği',
        'your_email@gmail.com',  # Gönderen
        ['recipient_email@gmail.com'],  # Alıcı
        fail_silently=False,
    )
    if created:
        ...
