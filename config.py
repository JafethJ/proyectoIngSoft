import os

class Config:
    DB_USER = 'proyectois'
    DB_PASSWORD = '1234'
    DB_NAME = 'formulario_db'
    DB_HOST = 'localhost'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave_secreta_segura'
