# Generated by Django 4.2.3 on 2024-01-05 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0006_transaction_expiry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 12, 14, 47, 27, 560482, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
