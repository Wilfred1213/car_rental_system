# Generated by Django 5.0.4 on 2024-05-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0016_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=1000)),
            ],
        ),
    ]
