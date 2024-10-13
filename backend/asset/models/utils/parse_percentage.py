from decimal import Decimal, InvalidOperation
import logging
from rest_framework import serializers

logger = logging.getLogger(f'{__name__}>Percentage')


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