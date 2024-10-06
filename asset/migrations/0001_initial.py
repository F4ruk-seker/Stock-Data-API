# Generated by Django 5.1 on 2024-09-08 08:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePublicAssetingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=500)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('request_start_date', models.DateField()),
                ('request_end_date', models.DateField()),
                ('lots_to_be_sold', models.BigIntegerField()),
                ('ipo_size', models.DecimalField(decimal_places=2, max_digits=15)),
                ('distribution_method', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SlotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progres_type', models.CharField(choices=[('t_sale', 't_sale'), ('t_1_sale', 't_1_sale'), ('t_2_sale', 't_2_sale'), ('buy', 'buy')], default='buy', max_length=10)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('action_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('action_time',),
            },
        ),
        migrations.CreateModel(
            name='AssetModel',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('logo', models.URLField(blank=True, default='', null=True)),
                ('url', models.URLField(blank=True, default='', null=True)),
                ('chart', models.URLField(blank=True, default='', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetPriceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.assetmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteAssetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.assetmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetOwnershipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking', models.BooleanField(default=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.assetmodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('slots', models.ManyToManyField(to='asset.slotmodel')),
            ],
        ),
    ]