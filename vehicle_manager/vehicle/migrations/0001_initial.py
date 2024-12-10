# Generated by Django 5.1.3 on 2024-11-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Economy', 'Economy'), ('SUV', 'SUV'), ('sedan', 'sedan'), ('Hatchback', 'Hatchback'), ('electric', 'electric'), ('Hybrid', 'Hybrid'), ('Sports car', 'Sports car'), ('Coupe', 'Coupe'), ('Utility', 'Utility')], default='Economy', max_length=200)),
                ('engine', models.CharField(choices=[('Inline', 'Inline'), ('v Engine', 'v Engine'), ('W Engine', 'W Engine'), ('OPOC', 'OPOC')], default='v Engine', max_length=100)),
                ('fuel', models.CharField(choices=[('PETROL', 'PETROL'), ('DIESEL', 'DIESEL'), ('CNG', 'CNG'), ('ELECTRIC', 'ELECTRIC')], default='PETROL', max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField()),
            ],
        ),
    ]