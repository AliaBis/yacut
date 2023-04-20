from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from settings import ALLOWED_CHARACTERS

from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите исходную ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256), URL(require_tld=True,
                    message=('Проверьте ссылку'))])
    custom_id = StringField(
        'Введите короткий вариант ссылки',
        validators=[Length(1, 16), Optional(),
                    Regexp(ALLOWED_CHARACTERS,
                    message='Используйте символы [A-Za-z0-9]')])
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
