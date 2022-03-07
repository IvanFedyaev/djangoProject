# Generated by Django 4.0.3 on 2022-03-07 19:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=50)),
                ('ru_departure', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('picture', models.URLField(max_length=300)),
                ('price', models.PositiveIntegerField()),
                ('stars', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('country', models.CharField(max_length=15)),
                ('nights', models.PositiveSmallIntegerField()),
                ('date', models.CharField(max_length=30)),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.departure')),
            ],
        ),
    ]
