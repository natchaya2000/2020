# Generated by Django 2.2 on 2020-01-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='rent',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
