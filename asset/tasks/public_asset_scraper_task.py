from celery import shared_task
from scrapers import ActivePublicOfferingScraper
from config.settings.base import ASSET_PUBLIC_OFFER_DATA_SOURCE
import logging


logger = logging.getLogger(__name__)


@shared_task
def regular_public_asset_data_acquisition(*args, **kwargs):
    from asset.models import ActivePublicAssetingModel
    from asset.api.serializers import ActivePublicAssetSerializer

    def is_public_asset_exists(**kwargs) -> bool:
        return ActivePublicAssetingModel.objects.filter(**kwargs).exists()

    if scraper := ActivePublicOfferingScraper(ASSET_PUBLIC_OFFER_DATA_SOURCE):
        create_serializer = ActivePublicAssetSerializer(
            data=[public_asset for public_asset in scraper if not is_public_asset_exists(url=public_asset.url)],
            many=True
        )
        if create_serializer.is_valid(raise_exception=True):
            create_serializer.save()
