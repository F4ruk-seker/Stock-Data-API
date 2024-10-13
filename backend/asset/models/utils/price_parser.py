from decimal import Decimal, InvalidOperation
import logging
from rest_framework import serializers

logger = logging.getLogger(f'{__name__}>Price')


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