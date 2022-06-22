from random import choice
from string import ascii_letters, digits

from django.conf import settings

SIZE = int(settings.SHORTENER_BLOCK_SIZE)

CHARACTERS = ascii_letters + digits


def generate_shortcode():
    return "".join(
        [choice(CHARACTERS) for _ in range(SIZE)]
    )
