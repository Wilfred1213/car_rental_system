# Generated by Django 5.0.4 on 2024-05-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0017_latestservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media')),
                ('body', models.TextField(max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
