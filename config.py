import os
from dotenv import load_dotenv
#from flask_sqlalchemy import SQLAlchemy

# Cargar variables del .env
load_dotenv()

class Config:
    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración fraccionada (opcional, si no usas DATABASE_URL completo)
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
