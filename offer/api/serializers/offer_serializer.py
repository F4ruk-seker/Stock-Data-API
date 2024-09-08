import logging
from rest_framework import serializers
from offer.models import OfferModel
from decimal import Decimal, InvalidOperation


# Logger'ı oluştur
logger = logging.getLogger(__name__)


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferModel
        # fields = '__all__'
        exclude: tuple = 'updated_by', 'price_flow'

    def to_internal_value(self, data):
        if not isinstance(data, dict):
            raise serializers.ValidationError('Expected a dictionary but got {}'.format(type(data).__name__))

        def parse_price(value):
            if not value:
                return Decimal('0.00')
            cleaned_value = value.replace('.', '').replace(',', '.').strip()
            try:
                return Decimal(cleaned_value)
            except InvalidOperation:
                error_message = f'Invalid price format: {value}'
                logger.error(error_message)
                raise serializers.ValidationError(error_message)

        # Yüzdeleri parse etme
        def parse_percentage(value):
            if not value:
                return None
            cleaned_value = value.replace('%', '').replace(',', '.').strip()
            try:
                return Decimal(cleaned_value)
            except InvalidOperation:
                error_message = f'Invalid percentage format: {value}'
                logger.error(error_message)
                raise serializers.ValidationError(error_message)

        internal_data = {
            'name': data.get('name'),
            'code': data.get('code'),
            'logo': data.get('logo'),
            'url': data.get('url'),
            'current_price': parse_price(data.get('current_price')),
            'max_price': parse_price(data.get('max_price')),
            'min_price': parse_price(data.get('min_price')),
            'percentage': parse_percentage(data.get('percentage')),
            'last_update': data.get('last_update'),
            'chart': data.get('chart'),
        }

        return super().to_internal_value(internal_data)
