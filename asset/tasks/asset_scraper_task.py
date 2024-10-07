from celery import shared_task
from scrapers import OfferScraper
from models import OfferModel
from config.settings.base import ASSET_OFFER_DATA_SOURCE


import logging

logger = logging.getLogger(__name__)


@shared_task
def regular_asset_data_acquisition():
    from asset.models import AssetModel
    from asset.api.serializers import AssetSerializer

    if scraper := OfferScraper(ASSET_OFFER_DATA_SOURCE):
        asset_list: list[OfferModel] = [asset for asset in scraper.data if asset.code]  # only asset has code
        asset_codes: list = [asset.code for asset in asset_list if asset.code]
        existing_records = {item.code: item for item in AssetModel.objects.filter(code__in=asset_codes)}
        bulk_update_data = [asset for asset in asset_list if asset.code in existing_records]
        bulk_create_data = [asset.__dict__ for asset in asset_list if asset.code not in existing_records]

        if bulk_update_data:
            for update_asset in bulk_update_data:
                if instance_asset := existing_records.get(update_asset.code, None):
                    serializer = AssetSerializer(instance_asset, data=update_asset.__dict__, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

        if bulk_create_data:
            create_serializer = AssetSerializer(data=bulk_create_data, many=True)
            create_serializer.is_valid(raise_exception=True)
            create_serializer.save()

