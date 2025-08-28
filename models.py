from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  

db = SQLAlchemy()

# =========================
# Tabla: Usuario
# =========================
class Usuario(db.Model):
    __tablename__ = "usuarios"   # Nombre de la tabla en la BD
    id = db.Column(db.Integer, primary_key=True)  # Columna ID autoincremental, clave primaria
    nombres = db.Column(db.String(50), nullable=False)  # Columna nombres (máx 50 chars, no nula)
    apellidos = db.Column(db.String(50), nullable=False)  # Columna apellidos (máx 50 chars, no nula)
    ci = db.Column(db.Integer, nullable=False)  # Columna CI (entero, no nula)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Columna fecha/hora de creación

    def __repr__(self):
        return f"<Usuario {self.nombres}>"  # Representación del objeto (para debug)

# =========================
# Tabla: Reporte
# =========================
class Reporte(db.Model):
    __tablename__ = "reporte"  # Nombre de la tabla en la BD
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    fecha = db.Column(db.String(50), nullable=False)  # Fecha como texto

    # Relación con Usuario (FK = Foreign Key)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    # Relación: un usuario tiene muchos reportes
    usuario = db.relationship("Usuario", backref="reportes")

# =========================
# Tabla: Archivos
# =========================
class Archivos(db.Model):
    __tablename__ = "archivos"  # Nombre de la tabla en la BD
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    formato = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.String(50), nullable=False)
    ubicacion = db.Column(db.String(50), nullable=False)

    # Relación con Reporte
    reporte_id = db.Column(db.Integer, db.ForeignKey("reporte.id"), nullable=False)

    # Relación: un reporte tiene muchos archivos
    reporte = db.relationship("Reporte", backref="archivos")

# =========================
# Tabla: Celular
# =========================
class Celular(db.Model):
    __tablename__ = "celular"  # Nombre de la tabla en la BD
    id = db.Column(db.Integer, primary_key=True)
    nombre_dispositivo = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    version =  db.Column(db.String(50), nullable=False)
    cpu =  db.Column(db.String(50), nullable=False)
    ram =  db.Column(db.String(50), nullable=False)
    rom =  db.Column(db.String(50), nullable=False)
    bateria =  db.Column(db.String(50), nullable=False)
    versionhios =  db.Column(db.String(50), nullable=False)
    numero_compilacion =  db.Column(db.String(50), nullable=False)
    

    # Relación con Reporte
    reporte_id = db.Column(db.Integer, db.ForeignKey("reporte.id"), nullable=False)

    # Relación: un reporte tiene muchos archivos
    reporte = db.relationship("Reporte", backref="celulares")