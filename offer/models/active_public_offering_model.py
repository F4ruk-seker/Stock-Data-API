from django.db import models


class ActivePublicOfferingModel(models.Model):
    # Satış Fiyatı: ₺15,30
    sales_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Satış Fiyatı'
    )

    # Talep Toplama: 29.08.2024 - 03.09.2024
    demand_collection_start = models.DateField(
        verbose_name='Talep Toplama Başlangıcı'
    )
    demand_collection_end = models.DateField(
        verbose_name='Talep Toplama Bitişi'
    )

    # Satılacak Lot: 100.000.000 Lot
    lots_to_sell = models.BigIntegerField(
        verbose_name='Satılacak Lot'
    )

    # Halka Arz Büyüklüğü: ₺1.530.000.000
    public_offering_size = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Halka Arz Büyüklüğü'
    )

    # Dağıtım Yöntemi: Bireysele Eşit
    DISTRIBUTION_METHOD_CHOICES = [
        ('Bireysele Eşit', 'Bireysele Eşit'),
        ('Diğer Yöntem', 'Diğer Yöntem'),  # Diğer olası yöntemler eklenebilir
    ]

    distribution_method = models.CharField(
        max_length=50,
        choices=DISTRIBUTION_METHOD_CHOICES,
        verbose_name='Dağıtım Yöntemi'
    )

    def __str__(self):
        return f"Offering {self.id}"
