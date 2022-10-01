from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

def user_directory_path(instance, filename):
    """Trouxe direto da documentação, para simplificar."""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    extension = filename.split(".")[-1]
    return f"user_{instance.user.id}/profile_pic.{extension}"

class Student(models.Model):

    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="perfil",
    )

    foto_perfil = models.ImageField(
        "Foto de perfil",
        blank=True,
        upload_to=user_directory_path,
        default="user_default/profile.jpg",
    )
    
    create_date  = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Perfil de {self.user.username}"

class Teacher(models.Model):
    
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="perfil",
    )
    
    foto_perfil = models.ImageField(
        "Foto de perfil",
        blank=True,
        upload_to=user_directory_path,
        default="user_default/profile.jpg", 
    )
    
    create_date  = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Perfil de {self.user.username}"
    
