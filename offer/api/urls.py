from django.urls import path
from .views import *

app_name: str = 'offer'

urlpatterns = [
    path('bulk/offers', OfferBulkCreateUpdateView.as_view(), name='offer_bulk'),
    path('bulk/public-offer', ActivePublicOfferBulkCreateView.as_view(), name='active_public_offer')
]+[
    # User API way
    path('favorites', FavoriteOffersListView.as_view(), name='favorites'),
    path('favorites/<code>', FavoriteCreateDeleteView.as_view(), name='favorite'),
    path('<code>/slot', SlotCreateView.as_view()),
    path('<code>/slot/<int:pk>', SlotRetrieveUpdateDestroyView.as_view())
    # path('slot')
    # path('slot CRUD')
    # path(' hisseler')
]
