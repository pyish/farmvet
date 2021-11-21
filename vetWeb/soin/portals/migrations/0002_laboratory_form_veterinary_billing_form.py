# Generated by Django 3.1.3 on 2021-11-21 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory_Form',
            fields=[
                ('vet_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portals.vet_forms')),
                ('farmer_username', models.CharField(max_length=12, verbose_name='Farmer Username')),
                ('category_ssp', models.CharField(max_length=12, verbose_name='Category of the spp')),
                ('sample', models.CharField(max_length=12, verbose_name='Samples collected')),
                ('name_animal', models.CharField(max_length=12, verbose_name='Namer of the animal')),
                ('date_of_submission', models.DateField(verbose_name='Date of submission')),
                ('idenfication', models.IntegerField(blank=True, null=True, verbose_name='ID number')),
                ('storage', models.CharField(max_length=100, verbose_name='Method of storage')),
                ('transportation', models.CharField(max_length=200, verbose_name='Transportation means')),
                ('expected_duration', models.CharField(max_length=100, verbose_name='Expected duration of the sampling process')),
                ('sample_collected_sick_animal', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='Y', max_length=5, null=True, verbose_name='Was the sample collected for sick animal?')),
                ('sample_collected_dead', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], default='Y', max_length=5, null=True, verbose_name='Was the sample collected from a dead animal?')),
                ('if_yes_sick', models.CharField(blank=True, max_length=100, null=True, verbose_name='If yes,state the signs shown by the cadaver')),
                ('findings', models.CharField(max_length=100, verbose_name='What was the laboratory findings?')),
                ('vet_name', models.CharField(max_length=12, verbose_name='Name of the Veterinary officer who collected the sample.')),
                ('laboratory_offficer', models.CharField(max_length=20, verbose_name='Name of the laboratory officer')),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Registration number')),
                ('Mobile_number', models.IntegerField(blank=True, null=True, verbose_name='Mobile number')),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinary_Billing_Form',
            fields=[
                ('vet_form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portals.vet_forms')),
                ('farmer_username', models.CharField(max_length=12, verbose_name='Farmer Username')),
                ('farmer_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location of the farmer.')),
                ('nature_of_problem', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nature of problem bill is done for.')),
                ('bill_paid', models.CharField(blank=True, max_length=100, null=True, verbose_name='Total amount billed.')),
                ('total_bill', models.CharField(blank=True, max_length=100, null=True, verbose_name='Total bill paid by the farmer.')),
                ('balance_due', models.CharField(blank=True, max_length=100, null=True, verbose_name='Balance due to be paid.')),
                ('agreed_date', models.DateField(blank=True, max_length=100, null=True, verbose_name='Agreed date of payment.')),
                ('suggest_payment', models.CharField(blank=True, choices=[('F', 'Full'), ('I', 'Instalments')], default='0', max_length=20, null=True, verbose_name='Suggest payment plan for the balance')),
                ('vet_name', models.CharField(max_length=12, verbose_name='Veterinary officer claiming the bill.')),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Registration number')),
                ('Mobile_number', models.IntegerField(blank=True, null=True, verbose_name='Mobile number')),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
