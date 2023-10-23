# Generated by Django 4.2.6 on 2023-10-23 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MissingPerson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("height", models.CharField(max_length=100)),
                ("weight", models.CharField(max_length=100)),
                ("birth_date", models.DateTimeField()),
                ("last_seen", models.DateTimeField()),
                ("description", models.TextField(blank=True, null=True)),
                ("photo_url", models.URLField(blank=True, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("reporter", models.CharField(max_length=50)),
            ],
        ),
    ]
