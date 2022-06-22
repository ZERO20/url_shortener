from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from apps.url_management.models import Shortener
from apps.url_management.serializers import UrlShortenerSerializer


class GenerateShortUrlAPIView(APIView):

    def post(self, request):
        serializer = UrlShortenerSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(dict(shortcode=serializer.data['shortcode']), status=status.HTTP_201_CREATED)


class DecodeUrlShortApiView(APIView):

    def get(self, request, shortcode):
        shortener = get_object_or_404(Shortener, shortcode=shortcode)
        return Response(dict(url=shortener.url), 200)


class RedirectUrlShortApiView(APIView):

    def get(self, request, shortcode):
        shortener = get_object_or_404(Shortener, shortcode=shortcode)
        return HttpResponseRedirect(shortener.url)
