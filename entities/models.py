from django.db import models
from django.contrib.auth import get_user_model

class Student(models.Model):
    
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="perfil",
    )

    def __str__(self) -> str:
        return f"Perfil de {self.user.username}"  # pylint: disable=E1101

