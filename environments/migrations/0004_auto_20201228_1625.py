# Generated by Django 3.1 on 2020-12-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0003_auto_20201228_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environments',
            name='ip',
            field=models.CharField(max_length=15),
        ),
    ]
