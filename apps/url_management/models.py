from django.db import models

# Create your models here.


class Shortener(models.Model):
    url = models.URLField()
    shortcode = models.URLField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Shortener'
        verbose_name_plural = 'Shorteners'

    def __str__(self):
        return f'{self.url} to {self.shortcode}'
