# Generated by Django 3.1.3 on 2020-12-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_auto_20201217_1956"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="document",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="expense",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]