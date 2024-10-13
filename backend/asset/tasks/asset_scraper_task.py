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

    def serializer_common(**kwargs) -> AssetSerializer:
        create_serializer = AssetSerializer(**kwargs)
        create_serializer.is_valid(raise_exception=True)
        create_serializer.save()
        return create_serializer

    if scraper := OfferScraper(ASSET_OFFER_DATA_SOURCE):
        asset_list: list[OfferModel] = [asset for asset in scraper if asset.code]  # only asset has code
        asset_codes: list[str] = [asset.code for asset in asset_list if asset.code]
        existing_records: dict = {item.code: item for item in AssetModel.objects.filter(code__in=asset_codes)}
        bulk_update_data: list[OfferModel] = [asset for asset in asset_list if asset.code in existing_records]
        bulk_create_data: list[dict] = [asset.__dict__ for asset in asset_list if asset.code not in existing_records]

        for update_asset in bulk_update_data:
            serializer_common(instance=existing_records.get(update_asset.code), data=update_asset.__dict__, partial=True)

        if bulk_create_data:
            serializer_common(data=bulk_create_data, many=True)
