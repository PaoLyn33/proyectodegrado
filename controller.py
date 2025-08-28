from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # 👈 importamos la configuración centralizada
import psycopg2

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # 👈 cargamos Config
    db.init_app(app)

    # Ejemplo de ruta
    @app.route('/')
    def home():
        return "Conexión exitosa con PostgreSQL 🚀"

    return app

# Función extra si quieres conexión manual con psycopg2
def get_db_connection():
    conn = psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    return conn


# Ejecutar la app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
