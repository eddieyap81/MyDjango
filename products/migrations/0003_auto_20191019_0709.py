# Generated by Django 2.2.6 on 2019-10-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191016_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
