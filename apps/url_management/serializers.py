from rest_framework import serializers

from apps.url_management.models import Shortener


class UrlShortenerSerializer(serializers.Serializer):
    url = serializers.URLField()
    shortcode = serializers.SerializerMethodField(read_only=True)

    def get_shortcode(self, obj):
        """
        Forms the url with the generated shortcode
        """
        scheme_host = self.context['request']._current_scheme_host
        return f'{scheme_host}/{obj.shortcode}'

    def create(self, validated_data):
        return Shortener.objects.create(**validated_data)
