from django.core.management.base import BaseCommand
from asset.models.asset_model import AssetPriceModel, AssetModel
from config.settings.base import DATASET_DIR
import json
from asset.models.utils import parse_price, parse_percentage


class Command(BaseCommand):
    help = 'Load test data from a JSON file'
    model = AssetModel

    def add_arguments(self, parser):
        parser.add_argument('data_file_name', type=str, help='Name of the data file to load')

    def handle(self, *args, **kwargs):
        data_file_name = kwargs['data_file_name']
        data = self.get_data(data_file_name)
        self.load_data(data)
        self.stdout.write(f'{len(data)} records loaded from {data_file_name}')

    def get_data(self, data_file_name):
        file_path = DATASET_DIR / data_file_name

        if not file_path.exists():
            self.stderr.write(self.style.ERROR(f'{data_file_name} not found in {DATASET_DIR}'))
            return

        with open(file_path, 'r', encoding='utf-8') as df:
            return json.loads(df.read())

    def load_data(self, data):
        def do_item(item):
            item.pop('last_update')
            item['current_price'] = parse_price(item.pop('current_price'))
            item['min_price'] = parse_price(item.pop('min_price'))
            item['max_price'] = parse_price(item.pop('max_price'))
            item['percentage'] = parse_percentage(item.pop('percentage'))
            return item

        data_list = [item for item in data if not self.model.objects.filter(code=item.get('code')).exists()]
        assets = [self.model(**do_item(item)) for item in data_list]

        self.model.objects.bulk_create(assets)

        for asset in assets:
            if asset.current_price is not None:
                AssetPriceModel.objects.create(current_price=asset.current_price, asset=asset)
