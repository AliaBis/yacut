import random
import string

from settings import LENGTH

from .models import URLMap


def get_unique_short_id():

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        short_id = ''.join(random.choice(chars) for _ in range(LENGTH))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
