from django.test import TestCase
from config.settings.test import TEST_DATA_DIR
import json
from django.shortcuts import reverse, resolve_url
from asset.models import AssetModel


class AssetBulkUpdateTest(TestCase):

    def setUp(self):
        super().setUp()
        self.data_file_name = 'asset_data.json'
        self.test_data = self.load_test_data()
        self.asset_url = resolve_url(reverse('api:asset:asset_bulk'))

    def load_test_data(self):
        with open(TEST_DATA_DIR / self.data_file_name, 'r', encoding='utf-8') as df:
            return json.loads(df.read())

    def test_create_assets(self):
        initial_count = AssetModel.objects.count()

        response = self.client.post(
            path=self.asset_url,
            data=json.dumps(self.test_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        final_count = AssetModel.objects.count()

        self.assertEqual(final_count, initial_count + len(self.test_data))

    def test_update_assets(self):
        response = self.client.post(
            path=self.asset_url,
            data=json.dumps(self.test_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        initial_assets = list(AssetModel.objects.all().values())

        response = self.client.post(
            path=self.asset_url,
            data=json.dumps(self.test_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        updated_assets = list(AssetModel.objects.all().values())

        self.assertEqual(len(updated_assets), len(initial_assets))

        for initial, updated in zip(initial_assets, updated_assets):
            initial.pop('updated_at', None)
            updated.pop('updated_at', None)
            self.assertEqual(initial, updated)
