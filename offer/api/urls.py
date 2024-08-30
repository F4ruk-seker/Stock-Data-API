from django.urls import path, include
from .views import *

app_name: str = 'offer'

urlpatterns = [
    path('offer', OfferBulkCreateUpdateView.as_view())
]
