# Generated by Django 4.2.15 on 2024-08-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_remove_pageseenmodel_browser"),
    ]

    operations = [
        migrations.AddField(
            model_name="pageseenmodel",
            name="csrf_coockie",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
