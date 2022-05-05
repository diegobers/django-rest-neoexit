from django.db import models
from django.conf import settings


class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"


class Oferta(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    title = models.TextField(max_length=100, null=True)
    slug = models.SlugField(unique=True, null=True)
    content = models.TextField(null=True)
    
    def __str__(self):
        return self.title