# Generated by Django 2.1.5 on 2019-02-12 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_auto_20190212_1334"),
        ("leads", "0004_auto_20190212_1334"),
        ("accounts", "0004_account_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="assigned_to",
        ),
        migrations.RemoveField(
            model_name="account",
            name="teams",
        ),
        migrations.AddField(
            model_name="account",
            name="contacts",
            field=models.ManyToManyField(
                related_name="account_contacts", to="contacts.Contact"
            ),
        ),
        migrations.AddField(
            model_name="account",
            name="leads",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="account_leads",
                to="leads.Lead",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="account_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
