from django.db import models

from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name="imagen", upload_to='blog')
    title = models.CharField(max_length=200, verbose_name="titulo")
    description = RichTextField(verbose_name="descripción")
    content = RichTextField(verbose_name="contenido")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title
