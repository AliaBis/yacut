from http import HTTPStatus

from flask import jsonify, request

from . import app
from .crud import (create_url_map, url_map_by_short_id,
                   validate_request_body)
from .error_handlers import InvalidAPIUsageError


@app.route('/api/id/', methods=['POST'])
def create_id():
    request_data = request.get_json(silent=True)
    validate_request_body(request_data)
    url_map = create_url_map(request_data)
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    url_map = url_map_by_short_id(short_id)
    if not url_map:
        raise InvalidAPIUsageError(
            'Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original})
