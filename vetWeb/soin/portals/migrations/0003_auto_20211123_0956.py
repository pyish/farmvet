# Generated by Django 3.1.3 on 2021-11-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0002_laboratory_form_veterinary_billing_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='vet_forms',
            name='is_lab_form',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vet_forms',
            name='is_vet_billing_form',
            field=models.BooleanField(default=False),
        ),
    ]