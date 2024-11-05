from rest_framework.test import APITestCase, APIClient
from faker import Faker
from django.contrib.auth.models import User
from django.shortcuts import reverse, resolve_url
from asset.models import AssetModel, FavoriteAssetModel, SlotModel, AssetOwnershipModel
from rest_framework import status
from typing import NoReturn, AnyStr


class SlotTest(APITestCase):
    def setUp(self) -> NoReturn:
        self.client = APIClient()
        self.fake_assets = self.create_fake_assets()
        self.user: User = User.objects.create_user(
            username='echo',
            password='echo12345!'
        )
        self.second_user: User = User.objects.create_user(
            username='BAD_BOY_666',
            password='echo12345!'
        )
        # self.client.force_authenticate(user=self.user)
        self.selected_asset: AssetModel = AssetModel.objects.first()

    @staticmethod
    def get_slot_create_url(asset_code: str) -> AnyStr:
        return resolve_url(reverse('api:asset:slot_create', kwargs={
            'code': asset_code
        }))

    @staticmethod
    def get_slot_retrieve_update_destroy_url(asset_code: str, slot_id: int) -> AnyStr:
        return resolve_url(reverse('api:asset:slot', kwargs={
            'code': asset_code,
            'pk': slot_id
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

    @staticmethod
    def get_asset_owner_ship_model(user: User, asset: AssetModel) -> AssetOwnershipModel:
        asset_ownership, created = AssetOwnershipModel.objects.get_or_create(
            asset=asset,
            owner=user,
        )
        return asset_ownership

    def test_user_cant_create_slot_without_asset_ownership(self) -> NoReturn:
        """Test User Can't Create Slot Without Asset Owner Ship"""
        self.client.force_authenticate(user=self.user)
        # self.get_asset_owner_ship_model(user=self.user, asset=self.selected_asset)
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
        self.get_asset_owner_ship_model(user=self.user, asset=self.selected_asset)
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
        self.client.force_authenticate(user=self.user)
        request = self.client.get(self.get_slot_create_url(self.selected_asset.code))
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, request.status_code)

    def test_user_can_only_update_own_slot(self):
        """Test User Can Only Update Own Slot"""

    def test_users_can_only_see_their_own_slots(self):
        """Users Can Only See Their Own Slots"""

        self.test_user_can_create_slot_with_asset_ownership()
        asset_owner_ship = AssetOwnershipModel.objects.first()
        slot = asset_owner_ship.slots.first()
        self.assertEqual(type(slot), SlotModel)

        # good boy
        request = self.client.get(
            self.get_slot_retrieve_update_destroy_url(
                asset_code=self.selected_asset.code,
                slot_id=slot.id
            )
        )
        self.assertEqual(status.HTTP_200_OK, request.status_code)

        # bad user
        self.client.logout()
        self.client.force_authenticate(user=self.second_user)
        request = self.client.get(
            self.get_slot_retrieve_update_destroy_url(
                asset_code=self.selected_asset.code,
                slot_id=slot.id
            )
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, request.status_code)
