from django.db import models

from apps.url_management.functions import generate_shortcode


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
        code = generate_shortcode()
        if cls.objects.filter(shortcode=code).exists():
            return cls.create_shortened_url()
        return code

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = self.create_shortened_url()
        super().save(*args, **kwargs)
