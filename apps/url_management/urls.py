from django.urls import path
from apps.url_management.views import GenerateShortUrlAPIView, DecodeUrlShortApiView, RedirectUrlShortApiView

urlpatterns = [
    path('generate/short/url/', GenerateShortUrlAPIView.as_view(), name='generate-short-url'),
    path('decode/short/url/<str:shortcode>', DecodeUrlShortApiView.as_view(), name='decode-short-url'),
    path('<str:shortcode>', RedirectUrlShortApiView.as_view(), name='redirect-short-url'),
]
