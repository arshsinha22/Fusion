# Generated by Django 3.1.5 on 2024-04-18 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateField(default=datetime.date(2024, 4, 18)),
        ),
    ]
