# Generated by Django 5.0.4 on 2024-05-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0013_rentcar_car_alter_rentcar_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentingInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('instruction', models.CharField(max_length=255)),
            ],
        ),
    ]
