# Generated by Django 5.0.4 on 2024-05-14 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0024_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_hours', models.CharField(max_length=100, null=True)),
                ('price', models.BigIntegerField(default=0)),
                ('fuel', models.CharField(max_length=100, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentalApp.category')),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
