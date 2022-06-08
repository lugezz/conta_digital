# Generated by Django 3.1 on 2020-09-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoices", "0009_invoice_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="tax",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
    ]
