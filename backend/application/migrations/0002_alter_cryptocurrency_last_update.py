# Generated by Django 3.2.16 on 2023-06-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]