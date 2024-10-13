from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.shortcuts import reverse, resolve_url
from rest_framework.status import *
from asset.models import AssetModel, FavoriteAssetModel
from faker import Faker


class FavoritesRetrieveCreateDestroyTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='echo',
            password='echo12345!'
        )
        self.token = self._get_jwt_token()
        self.client = APIClient()

        self.create_asset()
        self.favorites_url = resolve_url(reverse('api:asset:favorites'))

    def _get_jwt_token(self):
        """
        JWT token almak için yardımcı bir metod
        """
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    @staticmethod
    def create_asset():
        fake = Faker()
        for _ in range(10):
            AssetModel.objects.create(
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

    def test_favorite_compute_unit_cannot_accept_get_request(self):
        selected_test_asset = AssetModel.objects.first()
        url = resolve_url(reverse('api:asset:favorite', kwargs={'code': selected_test_asset.code}))

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_add_selected_favorite_asset(self):
        selected_test_asset = AssetModel.objects.first()
        url = resolve_url(reverse('api:asset:favorite', kwargs={'code': selected_test_asset.code}))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        response = self.client.post(url, {
            'asset': selected_test_asset.code,
        })
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        asset = response.json().get('asset')
        response = self.client.get(self.favorites_url)
        code = response.json()[0].get('code', None)

        self.assertEqual(asset, code)

    def test_cant_add_selected_favorite_asset_when_unauthorized(self):
        before_request_favorite_count: int = len(self.client.get(self.favorites_url).json())

        selected_test_asset = AssetModel.objects.first()
        url = resolve_url(reverse('api:asset:favorite', kwargs={'code': selected_test_asset.code}))

        response = self.client.post(url, {
            'asset': selected_test_asset.code,
        })
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

        after_request_favorite_count: int = len(self.client.get(self.favorites_url).json())

        self.assertEqual(before_request_favorite_count, after_request_favorite_count)

    def test_user_cant_see_favorites_when_unauthorized(self):
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_user_can_see_favorites_when_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.status_code, HTTP_200_OK)
