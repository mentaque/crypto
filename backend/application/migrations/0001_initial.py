# Generated by Django 3.2.16 on 2023-06-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=4, max_digits=25)),
                ('volume_24h', models.DecimalField(decimal_places=4, max_digits=25)),
                ('percent_change_1h', models.DecimalField(decimal_places=4, max_digits=25)),
                ('percent_change_24h', models.DecimalField(decimal_places=4, max_digits=25)),
                ('percent_change_7d', models.DecimalField(decimal_places=4, max_digits=25)),
                ('percent_change_30d', models.DecimalField(decimal_places=4, max_digits=25)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
