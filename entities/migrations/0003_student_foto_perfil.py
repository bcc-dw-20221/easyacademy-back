# Generated by Django 4.1 on 2022-09-28 21:26

from django.db import migrations, models
import entities.models


class Migration(migrations.Migration):

    dependencies = [
        ("entities", "0002_student_create_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="foto_perfil",
            field=models.ImageField(
                blank=True,
                default="user_default/profile.jpg",
                upload_to=entities.models.user_directory_path,
                verbose_name="Foto de perfil",
            ),
        ),
    ]