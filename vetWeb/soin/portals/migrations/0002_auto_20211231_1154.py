# Generated by Django 3.1.3 on 2021-12-31 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referal_Form',
            fields=[
                ('vet_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portals.vet_forms')),
                ('farmer_username', models.CharField(max_length=12, verbose_name='Farmer Username')),
                ('Mobile_number', models.IntegerField(blank=True, null=True, verbose_name='Mobile number')),
                ('case_referal', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='Y', max_length=20, verbose_name='Is the case referal to another vet?')),
                ('previous_treated', models.CharField(max_length=12, verbose_name='State the previous treated given')),
                ('state_prognosis', models.CharField(max_length=100, verbose_name='state the prognosis of the animal on referal.')),
                ('referal_date', models.DateField(verbose_name='Date of referal')),
                ('suggest_vet', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='Y', max_length=20, verbose_name='Do you suggest a vet to be referred to?')),
                ('if_yes_leave_phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='If yes,write phone number of the vet')),
                ('registration_number', models.CharField(max_length=15, verbose_name='Registration number of the vet')),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='vet_forms',
            name='is_referral_form',
            field=models.BooleanField(default=False),
        ),
    ]
