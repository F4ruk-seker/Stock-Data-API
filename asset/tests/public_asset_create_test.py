from django.test import TestCase
from config.settings.test import TEST_DATA_DIR
import json
from django.shortcuts import reverse, resolve_url


class ActivePublicAssetBulkUpdateTest(TestCase):

    def setUp(self):
        super().setUp()
        self.data_file_name = 'active_asset_test_data.json'
        self.test_data = self.load_test_data()
        self.target_url = resolve_url(reverse('api:asset:active_public_asset'))

    def load_test_data(self):
        with open(TEST_DATA_DIR / self.data_file_name, 'r', encoding='utf-8') as df:
            return json.loads(df.read())

    def test_create_active_public_asset(self):
        response = self.client.post(
            self.target_url,
            data=self.test_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

