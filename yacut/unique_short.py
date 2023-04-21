import random
import string

from settings import RANDOM_LINK_LENGTH

from .models import URLMap


def get_unique_short_id():

    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        short_id = ''.join(random.choice(chars) for _ in range(RANDOM_LINK_LENGTH))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
