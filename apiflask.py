from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración para PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:proyecto@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de ejemplo
class Usuario(db.Model):
    __tablename__ = 'usuarios'  # nombre de la tabla en Postgres
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

# Crear las tablas en la BD
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Conexión exitosa con PostgreSQL 🚀"

if __name__ == '__main__':
    app.run(debug=True)
