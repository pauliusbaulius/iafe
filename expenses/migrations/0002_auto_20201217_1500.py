# Generated by Django 3.1.3 on 2020-12-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="date",
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name="expense",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
