from django.urls import path
from .views import *

app_name: str = 'offer'

urlpatterns = [
    path('bulk/offers', OfferBulkCreateUpdateView.as_view(), name='offer_bulk')
]
