from django.urls import path, include
from .views import *

app_name: str = 'offer'

urlpatterns = [
    path('bulk/offers', OfferBulkCreateUpdateView.as_view())
]
