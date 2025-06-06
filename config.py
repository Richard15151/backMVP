import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:senai@localhost/mathmagic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
