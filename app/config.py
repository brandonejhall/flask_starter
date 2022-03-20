import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my-super-secret-key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://oxonqiihgumdxy:d064a94bb5a5735be92aeec3e3722962f043ebe35774b5e289607ea0574b2ded@ec2-18-210-191-5.compute-1.amazonaws.com:5432/d5uft718vapebq'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy a
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')