# Generated by Django 3.1.3 on 2022-04-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0003_auto_20220130_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral_form',
            name='referal_date',
            field=models.DateField(verbose_name='referal date'),
        ),
    ]
