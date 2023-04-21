from re import match

from settings import ALLOWED_CHARACTERS, FORBIDDEN_CHARACTERS

from . import db
from .error_handlers import InvalidAPIUsageError
from .models import URLMap
from .unique_short import get_unique_short_id


def validate_request_body(request_data):
    if not request_data:
        raise InvalidAPIUsageError('Отсутствует тело запроса')
    if 'url' not in request_data:
        raise InvalidAPIUsageError('"url" является обязательным полем!')
    if not match(FORBIDDEN_CHARACTERS, request_data['url']):
        raise InvalidAPIUsageError('Указан недопустимый URL')
    if not request_data.get('custom_id'):
        request_data['custom_id'] = get_unique_short_id()
    if not match(ALLOWED_CHARACTERS, request_data['custom_id']):
        raise InvalidAPIUsageError(
            'Указано недопустимое имя для короткой ссылки')
    if url_map_by_short_id(request_data['custom_id']):
        raise InvalidAPIUsageError(
            f'Имя "{request_data["custom_id"]}" уже занято.')


def create_url_map(request_data):
    url_map = URLMap()
    url_map.from_dict(request_data)
    db.session.add(url_map)
    db.session.commit()
    return url_map


def url_map_by_short_id(short_id):
    return URLMap.query.filter_by(short=short_id).first()
