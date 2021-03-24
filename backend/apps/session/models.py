from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    jump_rope_number = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(
        User, related_name="sessions", verbose_name="Créé par", on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        verbose_name="Créé le", auto_now_add=True)
    ending_at = models.DateTimeField(
        verbose_name="Terminé à", blank=True, null=True)

    def __str__(self):
        return f'Session créé par {self.created_by.username} le {self.created_at} : {self.jump_rope_number} sauts'
