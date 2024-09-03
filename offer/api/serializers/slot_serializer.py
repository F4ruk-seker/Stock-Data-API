from offer.models import SlotModel
from rest_framework import serializers


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotModel
        # fields: str = '__all__'
        exclude: tuple = 'action_time',
