from django.contrib.auth.models import User
from django.db import models


class AssetOwnershipModel(models.Model):
    objects = models.Manager()

    asset = models.ForeignKey('asset.AssetModel', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # piece = models.IntegerField(default=0)
    # purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    slots = models.ManyToManyField('asset.SlotModel')
    # sold = models.BooleanField(default=False)
    tracking = models.BooleanField(default=True)

    def get_general_status(self, base_price: float | None = None):
        if base_price is None:
            base_price = self.asset.current_price
        remaining_lots: float = .0
        total_profit: float = .0
        if slots := self.slots.all():
            for transaction in slots:
                if transaction.progres_type == transaction.ProgresType.BUY:
                    remaining_lots += transaction.quantity
                    # total_profit += float(transaction.price) * transaction.quantity
                    total_profit += transaction.quantity * float(base_price)
                else:
                    sold_lots = transaction.quantity
                    sale_price = float(transaction.price)
                    profit = sold_lots * (sale_price - float(base_price))
                    total_profit += profit
                    remaining_lots -= sold_lots
        return {
            'total_profit': f'{total_profit:.2f}',
            'remaining_lots': remaining_lots
        }

    # def get_slots(self) -> list:
    #     return self.slots
