# Generated by Django 3.1 on 2020-09-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0022_auto_20200609_1203"),
        ("marketing", "0013_blockeddomain_blockedemail"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailtemplate",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="marketing_emailtemplates_company",
                to="common.company",
            ),
        ),
    ]
