from django.test import TestCase
from django.conf import settings

from apps.url_management.models import Shortener

SIZE = int(settings.SHORTENER_BLOCK_SIZE)
URL = 'https://fondeadora.com/'


class ShortenerTests(TestCase):

    def setUp(self) -> None:
        self.shortener = Shortener.objects.create(url=URL)

    def test_generate_shortcode(self):
        self.assertNotEqual(self.shortener.shortcode, '')

    def test_shortcode_size(self):
        self.assertEqual(len(self.shortener.shortcode), SIZE)

    def