# Generated by Django 5.0.7 on 2024-07-29 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(max_length=300)),
                ('url', models.URLField(blank=True, null=True)),
                ('ingr01name', models.CharField(blank=True, max_length=25)),
                ('ingr01measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr01measamount', models.CharField(blank=True, max_length=15)),
                ('ingr02name', models.CharField(blank=True, max_length=25)),
                ('ingr02measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr02measamount', models.CharField(blank=True, max_length=15)),
                ('ingr03name', models.CharField(blank=True, max_length=25)),
                ('ingr04measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr04measamount', models.CharField(blank=True, max_length=15)),
                ('ingr04name', models.CharField(blank=True, max_length=25)),
                ('ingr05measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr06measamount', models.CharField(blank=True, max_length=15)),
                ('ingr06name', models.CharField(blank=True, max_length=25)),
                ('ingr06measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr07measamount', models.CharField(blank=True, max_length=15)),
                ('ingr08name', models.CharField(blank=True, max_length=25)),
                ('ingr08measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr08measamount', models.CharField(blank=True, max_length=15)),
                ('ingr09name', models.CharField(blank=True, max_length=25)),
                ('ingr10measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr10measamount', models.CharField(blank=True, max_length=15)),
                ('ingr10name', models.CharField(blank=True, max_length=25)),
                ('ingr11measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr12measamount', models.CharField(blank=True, max_length=15)),
                ('ingr12name', models.CharField(blank=True, max_length=25)),
                ('ingr12measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr13measamount', models.CharField(blank=True, max_length=15)),
                ('ingr14name', models.CharField(blank=True, max_length=25)),
                ('ingr14measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr14measamount', models.CharField(blank=True, max_length=15)),
                ('ingr15name', models.CharField(blank=True, max_length=25)),
                ('ingr15measunit', models.CharField(blank=True, choices=[('Teaspoons', 'tsp'), ('Table Spoons', 'TBSP'), ('1/4 Cup', '1/4 Cup'), ('1/3 Cup', '1/3 Cup'), ('1/2 Cup', '1/2 Cup'), ('1 Cup', 'Cup'), ('1 Pint', 'Pint'), ('1 Quart', 'Quart'), ('1 Gallon', 'Gallon')], max_length=15)),
                ('ingr15measamount', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('abbrev', models.CharField(blank=True, max_length=15)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recipe_sizer_app.measuretype')),
            ],
        ),
    ]