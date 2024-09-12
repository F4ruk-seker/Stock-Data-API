import logging
from rest_framework import serializers
from asset.models import AssetModel
from decimal import Decimal, InvalidOperation


# Logger'ı oluştur
logger = logging.getLogger(__name__)


class AssetSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        print(validated_data)

        if isinstance(validated_data, dict):
            code = validated_data.get('code')
            instance, created = AssetModel.objects.update_or_create(
                code=code,
                defaults=validated_data
            )
            return instance

        elif isinstance(validated_data, list):
            instances = [AssetModel(**data) for data in validated_data]
            return AssetModel.objects.bulk_create(instances)
        return None

    class Meta:
        model = AssetModel
        # fields = '__all__'
        exclude: tuple = 'updated_by',

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

