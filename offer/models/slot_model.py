from django.db import models
from datetime import timedelta, datetime
import pytz


class SlotModel(models.Model):
    objects = models.Manager()

    class ProgresType(models.TextChoices):
        T_SALE = 't_sale', 't_sale'
        T_1_SALE = 't_1_sale', 't_1_sale'
        T_2_SALE = 't_2_sale', 't_2_sale'
        BUY = 'buy', 'buy'

    progres_type = models.CharField(max_length=10, choices=ProgresType.choices, default=ProgresType.BUY)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    # action_time = models.DateTimeField(default=timezone.now, editable=True)
    action_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: tuple = 'action_time',

    @property
    def is_buy(self):
        return self.progres_type == self.ProgresType.BUY

    @property
    def is_sale_cooldown(self):
        # now = datetime.now()  # Get current datetime
        # now = now.replace(tzinfo=None)  # Make it offset-naive
        now = datetime.now(pytz.utc)  # Get current datetime with UTC timezone

        match self.progres_type:
            case self.ProgresType.BUY:
                return True
            case self.ProgresType.T_SALE:
                return self.action_time < now
            case self.ProgresType.T_1_SALE:
                return (self.action_time + timedelta(days=1)) < now
            case self.ProgresType.T_2_SALE:
                return (self.action_time + timedelta(days=2)) < now
