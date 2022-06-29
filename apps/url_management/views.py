from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from apps.url_management.models import Shortener
from apps.url_management.serializers import UrlShortenerSerializer


decode_response_schema_dict = {
    "200": openapi.Response(description="URL", examples={"application/json": {"url": "https://example.com/"}}),
    "404": openapi.Response(description="Not found", examples={"application/json": {"detail": "Not found."}})
}


redirect_response_schema_dict = {
    "302": openapi.Response(description="Redirect")
}


class GenerateShortUrlAPIView(APIView):
    """Generates a shortcode for a valid URL"""
    @swagger_auto_schema(request_body=UrlShortenerSerializer, tags=['Generate shortcode'])
    def post(self, request):
        serializer = UrlShortenerSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(dict(shortcode=serializer.data['shortcode']), status=status.HTTP_201_CREATED)


class DecodeUrlShortApiView(APIView):
    """Decodes a URL short into the original URL"""
    @swagger_auto_schema(responses=decode_response_schema_dict, tags=['Decode shortcode'])
    def get(self, request, shortcode):
        shortener = get_object_or_404(Shortener, shortcode=shortcode)
        return Response(dict(url=shortener.url), 200)


class RedirectUrlShortApiView(APIView):
    """Redirects to original URL when accessing URL short"""
    @swagger_auto_schema(responses=redirect_response_schema_dict, tags=['Redirect to original URL'])
    def get(self, request, shortcode):
        shortener = get_object_or_404(Shortener, shortcode=shortcode)
        return HttpResponseRedirect(shortener.url)
