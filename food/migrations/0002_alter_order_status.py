# Generated by Django 5.0.3 on 2024-12-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Finished', 'Finished')], default='Pending', max_length=20),
        ),
    ]
