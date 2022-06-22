from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string


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

    @classmethod
    def create_shortened_url(cls):
        code = get_random_string(int(settings.SHORTENER_BLOCK_SIZE))
        if cls.objects.filter(shortcode=code).exists():
            return cls.create_shortened_url()
        return code

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = self.create_shortened_url()
        super().save(*args, **kwargs)
