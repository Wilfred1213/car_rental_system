# Generated by Django 5.0.4 on 2024-05-14 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0028_pricingtier_carpricing_delete_pricing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carpricing',
            old_name='pricing_tier',
            new_name='pricing_tier_hour',
        ),
        migrations.RemoveField(
            model_name='carpricing',
            name='effective_date',
        ),
        migrations.RemoveField(
            model_name='carpricing',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='carpricing',
            name='pricing_tier_daily',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily', to='rentalApp.pricingtier'),
        ),
        migrations.AddField(
            model_name='carpricing',
            name='pricing_tier_leasing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leasing', to='rentalApp.pricingtier'),
        ),
    ]
