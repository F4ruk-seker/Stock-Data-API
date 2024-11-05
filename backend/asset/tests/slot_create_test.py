from rest_framework.test import APITestCase, APIClient
from faker import Faker
from django.contrib.auth.models import User
from django.shortcuts import reverse, resolve_url
from asset.models import AssetModel, FavoriteAssetModel, SlotModel, AssetOwnershipModel
from rest_framework import status
from typing import NoReturn, AnyStr


class SlotCreateTest(APITestCase):
    def setUp(self) -> NoReturn:
        self.client = APIClient()
        self.fake_assets = self.create_fake_assets()
        self.user: User = User.objects.create_user(
            username='echo',
            password='echo12345!'
        )
        self.client.force_authenticate(user=self.user)
        self.selected_asset: AssetModel = AssetModel.objects.first()

    @staticmethod
    def get_slot_create_url(slot_code: str) -> AnyStr:
        return resolve_url(reverse('api:asset:slot_create', kwargs={
            'code': slot_code
        }))

    @staticmethod
    def create_fake_assets(fake_asset_count: int = 10) -> list[AssetModel]:
        fake = Faker()
        assets = [
            AssetModel(
                name=fake.word(),
                code=fake.unique.word()[:10],
                current_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                max_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                min_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                percentage=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
                logo=fake.url(),
                url=fake.url(),
                chart=fake.url(),
            )
            for _ in range(fake_asset_count)
        ]
        AssetModel.objects.bulk_create(assets)
        return assets

    def get_asset_owner_ship_model(self, asset: AssetModel) -> AssetOwnershipModel:
        return AssetOwnershipModel.objects.create(
            asset=asset,
            owner=self.user,
        )

    def test_user_cant_create_slot_without_asset_ownership(self) -> NoReturn:
        """Test User Can't Create Slot Without Asset Owner Ship"""
        self.client.force_authenticate(user=self.user)
        # self.get_asset_owner_ship_model(asset=self.selected_asset)
        request = self.client.post(
            path=self.get_slot_create_url(self.selected_asset.code),
            data={
                'progres_type': SlotModel.ProgresType.BUY,
                'price': 10,
                'quantity': 1
            }
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, request.status_code)

    def test_user_can_create_slot_with_asset_ownership(self) -> NoReturn:
        """Test User Can Create Slot With Asset Ownership"""
        self.client.force_authenticate(user=self.user)
        self.get_asset_owner_ship_model(asset=self.selected_asset)
        request = self.client.post(
            path=self.get_slot_create_url(self.selected_asset.code),
            data={
                'progres_type': SlotModel.ProgresType.BUY,
                'price': 10,
                'quantity': 1
            }
        )
        self.assertEqual(status.HTTP_201_CREATED, request.status_code)

    def test_user_cant_get_request_at_the_slot_api(self) -> NoReturn:
        """Test User Cant Get Request At The Slot Api"""
        request = self.client.get(self.get_slot_create_url(self.selected_asset.code))
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, request.status_code)

    '''
        path('<code>/slot/<int:pk>', SlotRetrieveUpdateDestroyView.as_view()),
    '''