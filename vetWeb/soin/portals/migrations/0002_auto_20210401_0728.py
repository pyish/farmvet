# Generated by Django 3.1.3 on 2021-04-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deworming_form',
            name='number_of_young_ones',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Number of young ones'),
        ),
    ]
