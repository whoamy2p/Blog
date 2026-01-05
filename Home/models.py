from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='news/', verbose_name="Imagen")
    author = models.CharField(max_length=100, default="Admin", verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
