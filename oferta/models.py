from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


GRUPO = [
    ('Lancamento','Lancamento'),
    ('Destaque','Destaque'),
    ('Aberta','Aberta'),
    ('Fechada','Fechada'),
]

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil")
    bio = models.TextField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"

class Investimento(models.Model):
    creator_invest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateField(auto_now_add=True)
    value = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    cota_qtd = models.PositiveIntegerField(default=0)

class Comentario(models.Model):
    creator_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateField(auto_now_add=True)

class Oferta(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True)
    comentarios = GenericRelation(Comentario)
    investimentos = GenericRelation(Investimento)
    date_initial = models.DateField(null=True)
    date_end = models.DateField(null=True)
    value_total = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    cotas_total = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=200, null=True, choices=GRUPO)


    def __str__(self):
        return self.title
