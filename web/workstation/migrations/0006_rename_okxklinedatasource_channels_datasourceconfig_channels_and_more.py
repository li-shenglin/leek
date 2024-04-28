# Generated by Django 4.2.10 on 2024-04-24 07:29
import sys

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workstation', '0005_strategyconfig_factory_strategyconfig_price_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasourceconfig',
            old_name='okxklinedatasource_channels',
            new_name='channels',
        ),
        migrations.RenameField(
            model_name='datasourceconfig',
            old_name='okxklinedatasource_symbols',
            new_name='symbols',
        ),
        migrations.RenameField(
            model_name='datasourceconfig',
            old_name='okxklinedatasource_url',
            new_name='wsurl',
        ),
        migrations.AddField(
            model_name='datasourceconfig',
            name='inst_type',
            field=models.CharField(choices=[('SPOT', '币币'), ('MARGIN', '币币杠杆'), ('SWAP', '永续合约'), ('FUTURES', '交割合约'), ('OPTION', '期权')], default='SWAP', max_length=20, verbose_name='交易产品'),
        ),
        migrations.AddField(
            model_name='datasourceconfig',
            name='interval',
            field=models.IntegerField(default='300', verbose_name='行情刷新周期(秒)'),
        )
    ]
    if "migrate" in sys.argv:
        db = [arg.split("=")[1] for arg in sys.argv if arg.startswith("--database")]
        if len(db) > 0 and db[0] == "data":
            operations = []