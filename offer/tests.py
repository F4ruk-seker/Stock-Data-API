from django.test import TestCase
from config.settings.test import TEST_DATA_DIR
import json
from django.shortcuts import reverse, resolve_url
from offer.models import OfferModel


class OfferBulkUpdateTest(TestCase):

    def setUp(self):
        super().setUp()
        self.test_data = self.load_test_data()
        self.offer_url = resolve_url(reverse('api:offer:offer_bulk'))

    @staticmethod
    def load_test_data():
        with open(TEST_DATA_DIR / 'offer_data.json', 'r', encoding='utf-8') as df:
            return json.loads(df.read())

    def test_create_offers(self):
        initial_count = OfferModel.objects.count()

        response = self.client.post(
            path=self.offer_url,
            data=json.dumps(self.test_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        final_count = OfferModel.objects.count()

        self.assertEqual(final_count, initial_count + len(self.test_data))

    def test_update_offers(self):
        # Create initial offers
        response = self.client.post(
            path=self.offer_url,
            data=json.dumps(self.test_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        # Fetch the initial offers from the database
        initial_offers = list(OfferModel.objects.all().values())

        # Update the offers with the same data
        response = self.client.post(
            path=self.offer_url,
            data=json.dumps(self.test_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        # Fetch the offers after update
        updated_offers = list(OfferModel.objects.all().values())

        # Verify the number of offers did not change
        self.assertEqual(len(updated_offers), len(initial_offers))

        # Verify that the offers before and after the update are identical, excluding 'updated_at'
        for initial, updated in zip(initial_offers, updated_offers):
            # Exclude 'updated_at' field from comparison
            initial.pop('updated_at', None)
            updated.pop('updated_at', None)
            self.assertEqual(initial, updated)
