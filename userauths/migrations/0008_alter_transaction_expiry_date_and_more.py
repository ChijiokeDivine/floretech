# Generated by Django 4.2.3 on 2024-01-06 09:45

import datetime
from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0007_alter_transaction_expiry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 13, 9, 45, 44, 738565, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_id",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=20,
                max_length=30,
                prefix="TRX",
                unique=True,
            ),
        ),
    ]
