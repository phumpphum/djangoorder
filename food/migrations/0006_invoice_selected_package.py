# Generated by Django 5.0.3 on 2025-01-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_dish_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='selected_package',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
