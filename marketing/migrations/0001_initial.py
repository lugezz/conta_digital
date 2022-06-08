# Generated by Django 2.1.7 on 2019-02-25 13:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=5000)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("schedule_date_time", models.DateTimeField(blank=True, null=True)),
                (
                    "reply_to_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("subject", models.CharField(max_length=5000)),
                ("html", models.TextField()),
                ("html_processed", models.TextField(blank=True, default="")),
                (
                    "from_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("from_name", models.EmailField(blank=True, max_length=254, null=True)),
                ("sent", models.IntegerField(blank=True, default="0")),
                ("opens", models.IntegerField(blank=True, default="0")),
                ("opens_unique", models.IntegerField(blank=True, default="0")),
                ("bounced", models.IntegerField(default="0")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Scheduled", "Scheduled"),
                            ("Cancelled", "Cancelled"),
                            ("Sending", "Sending"),
                            ("Preparing", "Preparing"),
                            ("Sent", "Sent"),
                        ],
                        default="Preparing",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CampaignLinkClick",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_address", models.GenericIPAddressField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "user_agent",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="marketing.Campaign",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CampaignLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "message_id",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="campaign_contacts",
                        to="marketing.Campaign",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CampaignOpen",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip_address", models.GenericIPAddressField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "user_agent",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="marketing.Campaign",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=500)),
                ("email", models.EmailField(max_length=254)),
                (
                    "contact_number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 20 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("is_unsubscribed", models.BooleanField(default=False)),
                ("is_bounced", models.BooleanField(default=False)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("last_name", models.CharField(blank=True, max_length=500, null=True)),
                ("city", models.CharField(blank=True, max_length=500, null=True)),
                ("state", models.CharField(blank=True, max_length=500, null=True)),
                ("contry", models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ContactList",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=500)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="marketing_contactlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmailTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=5000)),
                ("subject", models.CharField(max_length=5000)),
                ("html", models.TextField()),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="marketing_emailtemplates",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original", models.URLField(max_length=2100)),
                ("clicks", models.IntegerField(default="0")),
                ("unique", models.IntegerField(default="0")),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="marketing_links",
                        to="marketing.Campaign",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                (
                    "color",
                    models.CharField(
                        default="#999999", max_length=20, verbose_name="color"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="marketing_tags",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contactlist",
            name="tags",
            field=models.ManyToManyField(to="marketing.Tag"),
        ),
        migrations.AddField(
            model_name="contactlist",
            name="visible_to",
            field=models.ManyToManyField(
                related_name="contact_lists_visible_to", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="contact_list",
            field=models.ManyToManyField(
                related_name="contacts", to="marketing.ContactList"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="marketing_contacts_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="campaignopen",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="marketing.Contact",
            ),
        ),
        migrations.AddField(
            model_name="campaignlog",
            name="contact",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="marketing_campaign_logs",
                to="marketing.Contact",
            ),
        ),
        migrations.AddField(
            model_name="campaignlinkclick",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="marketing.Contact",
            ),
        ),
        migrations.AddField(
            model_name="campaignlinkclick",
            name="link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="marketing.Link",
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="contact_lists",
            field=models.ManyToManyField(
                related_name="campaigns", to="marketing.ContactList"
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="marketing_campaigns_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="email_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="marketing.EmailTemplate",
            ),
        ),
    ]
