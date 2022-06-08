# Generated by Django 2.1.5 on 2019-02-04 06:12

from django.db import migrations, models


def generate_status(apps, schema_editor):
    Account = apps.get_model("accounts", "Account")
    for account in Account.objects.all():
        account.status = "open"
        account.save()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_auto_20190201_1840"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="status",
            field=models.CharField(
                choices=[("open", "Open"), ("close", "Close")],
                default="open",
                max_length=64,
            ),
        ),
        migrations.RunPython(generate_status),
    ]
