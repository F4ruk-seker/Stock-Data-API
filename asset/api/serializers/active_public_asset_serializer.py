from datetime import datetime
from decimal import Decimal, InvalidOperation

from rest_framework import serializers
from asset.models import ActivePublicAssetingModel


class ActivePublicAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivePublicAssetingModel
        fields: str = '__all__'

    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, '%d.%m.%Y').date()

    @staticmethod
    def parse_price(price_str):
        try:
            # Print or log the price_str for debugging
            # print(f"Parsing price: {price_str}")

            # Remove unwanted characters and convert to Decimal
            clean_str = price_str.replace('₺', '').replace('.', '').replace(',', '.').strip()

            # Print or log the cleaned string for debugging
            # print(f"Cleaned price string: {clean_str}")

            # Convert to Decimal
            return Decimal(clean_str)

        except (InvalidOperation, ValueError) as e:
            # Handle the exception, e.g., log the error and return a default value or raise a more informative error
            print(f"Error parsing price: {price_str} - {e}")
            # You can return a default value or raise an exception here
            return Decimal('0.00')  # Example default value

    def to_internal_value(self, data):
        if not isinstance(data, dict):
            raise serializers.ValidationError('FR44 > Expected a dictionary but got {}'.format(type(data).__name__))

        details_dict = data.get('detail')

        return super().to_internal_value({
            'title': data['title'],
            'url': data['url'],
            'sale_price': self.parse_price(details_dict['Satış Fiyatı']),
            'request_start_date': self.parse_date(details_dict['Talep Toplama'].split(' - ')[0]),
            'request_end_date': self.parse_date(details_dict['Talep Toplama'].split(' - ')[1]),
            'lots_to_be_sold': int(details_dict['Satılacak Lot'].replace(' Lot', '').replace('.', '').replace(',', '')),
            'ipo_size': self.parse_price(details_dict['Halka Arz Büyüklüğü']),
            'distribution_method': details_dict['Dağıtım Yöntemi']
        })

