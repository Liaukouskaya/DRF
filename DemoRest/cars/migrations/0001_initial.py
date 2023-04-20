# Generated by Django 4.2 on 2023-04-19 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Vin')),
                ('color', models.CharField(max_length=65, verbose_name='Color')),
                ('brand', models.CharField(max_length=64, verbose_name='Brand')),
                ('car_type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Universal'), (3, 'Hatchback')], verbose_name='Car_Type')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
