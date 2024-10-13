from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from faker import Faker
from django.contrib.auth.models import User
from django.shortcuts import reverse, resolve_url
from asset.models import AssetModel, FavoriteAssetModel


class SlotCreateTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.token = self._get_jwt_token()
        self.user = User.objects.create_user(
            username='echo',
            password='echo12345!'
        )

    @staticmethod
    def create_asset():
        fake = Faker()
        for _ in range(10):  # Adjust the range for the number of fake assets you want to create
            AssetModel.objects.create(
                name=fake.word(),
                code=fake.unique.word()[:10],  # Ensure the code is unique and of length 10
                current_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                max_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                min_price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                percentage=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
                logo=fake.url(),
                url=fake.url(),
                chart=fake.url(),
            )

    def test_create_slot(self):
        print(self.client.request())

    def _get_jwt_token(self):
        """
        JWT token almak için yardımcı bir metod
        """
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)