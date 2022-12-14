# Generated by Django 4.1 on 2022-09-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ults", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="classhours",
            name="time_class",
            field=models.CharField(
                choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")], max_length=1
            ),
        ),
    ]
