# Generated by Django 4.1 on 2022-09-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ults", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="classhours",
            name="time_class",
            field=models.CharField(
                choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")], max_length=1
            ),
        ),
    ]