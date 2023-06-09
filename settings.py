import os


ALLOWED_CHARACTERS = r'^[A-Za-z0-9]{1,16}$'
FORBIDDEN_CHARACTERS = r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$'
RANDOM_LINK_LENGTH = 6


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')
