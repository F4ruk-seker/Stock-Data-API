from django.urls import path
from .views import *

app_name: str = 'asset'
urlpatterns = [
    path('bulk/assets', AssetBulkCreateUpdateView.as_view(), name='asset_bulk'),
    path('bulk/public-assets', ActivePublicAssetBulkCreateView.as_view(), name='active_public_asset')
]+[
    # User API way
    path('mine', AssetOwnerListView.as_view()),
    path('favorites', FavoriteAssetsListView.as_view(), name='favorites'),
    path('favorites/<code>', FavoriteCreateDeleteView.as_view(), name='favorite'),
    path('<code>/slot', SlotCreateView.as_view()),
    path('<code>/slot/<int:pk>', SlotRetrieveUpdateDestroyView.as_view()),
    path('code-and-name', AssetSummaryListView.as_view()),
    path('<code>', AssetDetailView.as_view()),
    path('', AssetListView.as_view()),
]
