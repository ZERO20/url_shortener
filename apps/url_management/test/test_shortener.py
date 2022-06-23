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

    def test_shortcode_exists(self):
        new_shortcode = Shortener.create_shortened_url()
        shorcode_exists = Shortener.objects.filter(shortcode=new_shortcode).exists()
        self.assertIs(shorcode_exists, False)
