from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.url_management.models import Shortener

URL = 'https://fondeadora.com/'


class AccountTests(APITestCase):
    """Test endpoints"""

    def test_generate_shortcode(self):
        generate_url = reverse('generate-short-url')
        data = {'url': URL}
        response = self.client.post(generate_url, data, format='json')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('shortcode', response_json)
        self.assertEqual(Shortener.objects.count(), 1)
        self.assertEqual(Shortener.objects.get().url, URL)

    @staticmethod
    def setup_shortener():
        return Shortener.objects.create(url=URL)

    def test_decode_shortcode(self):
        shortener = self.setup_shortener()
        shortcode = shortener.shortcode
        decode_url = reverse('decode-short-url', kwargs={'shortcode': shortcode})
        response = self.client.get(decode_url, format='json')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('url', response_json)
        self.assertEqual(response_json.get('url'), shortener.url)

    def test_redirect_shortcode(self):
        shortener = self.setup_shortener()
        shortcode = shortener.shortcode
        redirect_url = reverse('redirect-short-url', kwargs={'shortcode': shortcode})
        response = self.client.get(redirect_url, format='json')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, shortener.url)
